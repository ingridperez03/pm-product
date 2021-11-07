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
    
    data.info()
    indicador = Indicador(data, range(2000, 2021), "municipi", "unitats")
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
    
    data.info()
    indicador = Indicador(data, range(2000, 2021), "municipi", "unitats")
    return indicador

'''
    Neteja dades referents als naixements per dona (NPD) / fertilitat (F)
'''
def initF():
    data = pd.DataFrame()
    for any in [1991, 2011]:
        nomArxiu = "NPD_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(data_path, 'fertilitat', nomArxiu), encoding='latin-1', index_col=None)
        
        # Preprocessing necessari 
        dataAny["Any"] = any

        # Editar file columna 0 te un espai davant 
        # Remove unnecessari columns
        dataAny.drop([' 0', '1', '2', '3', '4 i més', 'Total Dones', 'Total Fills'], axis = 1, inplace=True)
        dataAny.rename(columns={" Nombre fills mitjà per dona": "Nombre fills mitjà per dona"}, inplace=True)
        
        data = data.append(dataAny)

    data.info()
    indicador = Indicador(data, [1991, 2011], "municipi", "unitats")
    return indicador

'''
    Netejar dades referents a la migracions (M)
'''
def initM():
    data = pd.DataFrame()
    for any in range(2000, 2021):
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
        'Migracions externes  immigracions', 'Migracions externes  emigracions'], axis = 1, inplace=True)

        data = data.append(dataAny)

    data.info()
    indicador = Indicador(data, range(2000, 2021), "municipi", "unitats")
    return indicador

def initDemografica():
    dimensio = Dimensio()

    # Creixement Població
    creixement = initCP()
    dimensio.afegirIndicador("Creixement Poblacio", creixement)

    # Index Envelliment
    envelliment = initIE()
    dimensio.afegirIndicador("Index Envelliment", envelliment)

    # Fertilitat 
    fertilitat = initF()
    dimensio.afegirIndicador("Fertilitat", fertilitat)

    # Migracions
    # migracions = initM()
    # dimensio.afegirIndicador("Migracions", migracions)

    return dimensio