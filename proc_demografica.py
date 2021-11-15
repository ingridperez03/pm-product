import pandas as pd
import os
from dimensio import Dimensio
from indicador import Indicador

# Localització path dades demografia
data_path = os.path.join('dades', 'demografia')

'''
    Neteja dades referents al creixement població (CP)
'''
def initCP():
    data = pd.DataFrame()
    for any in range(2000, 2021):
        nomArxiu = "CP_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(data_path, 'creixement_poblacio', nomArxiu), index_col=None)
        # Preprocessing necessari 
        dataAny["Any"] = any

        # Total total 
        dataAny['Total'] = dataAny['Total. De 0 a 14 anys'] + dataAny['Total. De 15 a 64 anys'] + dataAny['Total. 65 anys o més']

        # Total per sexes 
        dataAny['Homes'] = dataAny['Homes. De 0 a 14 anys'] + dataAny['Homes. De 15 a 64 anys'] + dataAny['Homes. 65 anys o més']
        dataAny['Dones'] = dataAny['Dones. De 0 a 14 anys'] + dataAny['Dones. De 15 a 64 anys'] + dataAny['Dones. 65 anys o més']

        # Total per grups d'edat
        dataAny['0-14 Anys'] = dataAny['Homes. De 0 a 14 anys'] + dataAny['Dones. De 0 a 14 anys']
        dataAny['15-64 Anys'] = dataAny['Homes. De 15 a 64 anys'] + dataAny['Dones. De 15 a 64 anys']
        dataAny['64 o més'] = dataAny['Homes. 65 anys o més'] + dataAny['Dones. 65 anys o més']

        dataAny.drop(['Homes. De 0 a 14 anys', 'Dones. De 0 a 14 anys', 'Homes. De 15 a 64 anys', 
                      'Dones. De 15 a 64 anys', 'Homes. 65 anys o més', 'Dones. 65 anys o més',
                      'Total. De 0 a 14 anys', 'Total. De 15 a 64 anys', 'Total. 65 anys o més'], axis = 1, inplace=True)
        
        data = data.append(dataAny)
    
    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)
    
    indicador = Indicador(data, range(2000, 2021), "municipi", "nombre persones")
    return indicador

'''
    Neteja dades referents als índexs d'envelliment i de sobreenvelliment
'''
def initIE():
    data = pd.DataFrame()
    for any in range(2000, 2021):
        nomArxiu = "IE_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(data_path, 'index_envelliment', nomArxiu), index_col=None)
        # Preprocessing necessari 
        dataAny["Any"] = any

        dataAny.drop(["% 0 a 15 anys", "% 16 a 64 anys", "% 65 anys i més", 
                      "Índex de dependència juvenil", "Índex de dependència de la gent gran", 
                      "Índex de dependència global"], axis = 1, inplace=True)
        
        if any == 2000 or any == 2001:
            dataAny.drop([2, 12], inplace=True)
        
        data = data.append(dataAny)
    
    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)
    
    indicador = Indicador(data, range(2000, 2021), "municipi", "index")
    return indicador


'''
    Netejar dades referents a la migracions (M)
'''
def initM():
    data = pd.DataFrame()
    for any in range(2002, 2021):
        nomArxiu = "M_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(data_path, 'migracions', nomArxiu), index_col=None)
        
        # Preprocessing necessari 
        dataAny["Any"] = any

        # Suma migracions 
        dataAny['Immigracions'] = dataAny['Migracions internes  amb la resta de Catalunya  immigracions'] + dataAny["Migracions internes  amb la resta d'Espanya  immigracions"] + dataAny['Migracions externes  immigracions']
        dataAny['Emigracions'] = dataAny['Migracions internes  amb la resta de Catalunya  emigracions'] + dataAny["Migracions internes  amb la resta d'Espanya  emigracions"] + dataAny['Migracions externes  emigracions']
        
        # Remove unnecessary columns 
        dataAny.drop(['Migracions internes  amb la resta de Catalunya  immigracions', 'Migracions internes  amb la resta de Catalunya  emigracions',
                      "Migracions internes  amb la resta d'Espanya  immigracions", "Migracions internes  amb la resta d'Espanya  emigracions", 
                      'Migracions externes  immigracions', 'Migracions externes  emigracions', "Migracions internes  amb la resta de Catalunya  saldo migratori", 
                      "Migracions internes  amb la resta d'Espanya  saldo migratori", "Migracions externes  saldo migratori"], axis = 1, inplace=True)

        data = data.append(dataAny)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2000, 2021), "municipi", "nombre persones")
    return indicador


def initDemografica():
    dimensio = Dimensio()

    # Creixement Població
    creixement = initCP()
    dimensio.afegirIndicador("Creixement Poblacio", creixement)

    # Index Envelliment
    envelliment = initIE()
    dimensio.afegirIndicador("Index Envelliment", envelliment)

    # Migracions
    migracions = initM()
    dimensio.afegirIndicador("Migracions", migracions)

    return dimensio

def exportarDemografica(dimensio):
    dades = pd.DataFrame()
    i = 0
    for indicador in dimensio.dades.keys():
        dadesInd = dimensio.dades[indicador].dades
        if i == 0:
            dades = dadesInd.copy(deep=True)
        else:
            dades = pd.merge(dades, dadesInd, on=["Literal", "Any", "Codi"], how='outer')
        i += 1

    dades.to_csv(os.path.join('dades', 'resultat', "demografica.csv"))