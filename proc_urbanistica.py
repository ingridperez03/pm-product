import os
import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

# Path localització dades urbanistiques
data_path = os.path.join('dades', 'urbanistica')
municipis = pd.read_csv(os.path.join('dades', 'noms_municipis.csv'))

'''
    Netejar dades referents als serveis (Se)
'''
def initSe():
    data = pd.DataFrame()
    path = os.path.join(data_path,'serveis')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path, nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '12_A2_SUC']]
        dataAny = pd.merge(dataAny, municipis, on="NomMun")
        dataAny.drop(columns={"NomMun", "Codi_ine_6_txt"} , inplace=True)
        dataAny.rename(columns={'Municipi':'Literal', '12_A2_SUC':'Serveis'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)

    indicador = Indicador(data, range(2012, 2021), "municipi", "hectarees")
    return indicador


'''
    Netejar dades referents als solars (So)
'''
def initSo():
    data = pd.DataFrame()
    path = os.path.join(data_path, 'solar')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path, nomArxiu))
        #print(dataAny)
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '15_Qual_SUC_SISTEMES']]
        dataAny = pd.merge(dataAny, municipis, on="NomMun")
        dataAny.drop(columns={"NomMun", "Codi_ine_6_txt"}, inplace=True)
        dataAny.rename(columns={'Municipi':'Literal', '15_Qual_SUC_SISTEMES':'Solar'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)
    
    indicador = Indicador(data, range(2012, 2021), "municipi", "hectarees")
    return indicador


'''
    Netejar dades referents a les zones_verdes (ZV)
'''
def initZV():
    data = pd.DataFrame()
    path = os.path.join(data_path, 'zones_verdes')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path, nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '15_SV_SUC']]
        dataAny = pd.merge(dataAny, municipis, on="NomMun")
        dataAny.drop(columns={"NomMun", "Codi_ine_6_txt"}, inplace=True)
        dataAny.rename(columns={'Municipi':'Literal', '15_SV_SUC':'Zones verdes'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2012, 2021), "municipi", "hectarees")
    return indicador


'''
    Netejar dades referents als equipaments (E)
'''
def initE():
    data = pd.DataFrame()
    path = os.path.join(data_path, 'equipaments')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path, nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '20_Equip_habt']]
        dataAny = pd.merge(dataAny, municipis, on="NomMun")
        dataAny.drop(columns={"NomMun", "Codi_ine_6_txt"}, inplace=True)
        dataAny.rename(columns={'Municipi':'Literal', '20_Equip_habt':'Equipament'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)
 
    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2012, 2021), "municipi", "m2 per habitant")
    return indicador


'''
    Netejar dades referents a la connectivitat (Con)
'''
def initCon():
    data = pd.DataFrame()
    path = os.path.join(data_path, 'connectivitat')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path, nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '15_SF_SUC', '15_SX1_SUC', '15_SX2_SUC']]
        dataAny = pd.merge(dataAny, municipis, on="NomMun")
        dataAny.drop(columns={"NomMun", "Codi_ine_6_txt"}, inplace=True)
        dataAny.rename(columns={'Municipi':'Literal', '15_SF_SUC':'Ferroviari', '15_SX1_SUC':'Camins Principals', '15_SX2_SUC':'Camins Secundaris'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data["Connectivitat"] = data[["Ferroviari", "Camins Principals", "Camins Secundaris"]].sum(axis=1)
    data.drop(["Ferroviari", "Camins Principals", "Camins Secundaris"], axis=1, inplace=True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2012, 2021), "municipi", "hectarees")
    return indicador


'''
    Netejar dades referents al comerç
'''
def initCom():
    data = pd.DataFrame()
    path = os.path.join(data_path, 'comerç')

    for any in range(2017, 2020):
        nomArxiu = "comerç_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path, nomArxiu))
        dataAny = dataAny[['Any', 'Municipi', 'Codi_ine_6_txt', 'Densitat comercial (m2 / 1.000 hab.)']]
        dataAny.rename(columns={'Municipi':'Literal', 'Codi_ine_6_txt':'Codi', 'Densitat comercial (m2 / 1.000 hab.)':'Densitat comercial'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2017, 2020), "municipi", "m2 per mil habitants")
    return indicador


'''
    Netejar dades referents als riscos
'''
def initR():
    data = pd.DataFrame()
    path = os.path.join(data_path,'riscos')

    nomArxiu = "riscos.csv"
    dataAny = pd.read_csv(os.path.join(path, nomArxiu))
    dataAny = dataAny[['municipiNom', 'ine6', 'nivell']]
    dataAny = dataAny.rename(columns={'municipiNom':'NomMun'})
    dataAny = pd.merge(dataAny, municipis, on="NomMun")
    dataAny.drop(columns={"NomMun", "ine6"}, inplace=True)
    dataAny = dataAny.rename(columns={'Municipi':'Literal', 'nivell':'Nivell'})
    dataAny["Any"] = 2020
    data = data.append(dataAny, ignore_index = True)

    group = data.groupby(['Literal', 'Codi', 'Any'])
    data = group.size().reset_index(name='Riscos')

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, 2021, "municipi", "nombre de riscos")
    return indicador


def initUrbanistica():
    dimensio = Dimensio()

    # Serveis - Canviar municipis noms
    serveis = initSe()
    dimensio.afegirIndicador("Serveis", serveis)

    # Solar - Canviar municipis noms
    solar = initSo()
    dimensio.afegirIndicador("Solar", solar)

    # Zones verdes - Canviar municipis noms
    zones_verdes = initZV()
    dimensio.afegirIndicador("Zones verdes", zones_verdes)

    # Equipaments - Canviar municipis noms
    equipament = initE()
    dimensio.afegirIndicador("Equipament", equipament)

    # Connectivitat - Canviar municipis noms
    connectivitat = initCon()
    dimensio.afegirIndicador("Connectivitat", connectivitat)

    # Comerç
    comerç = initCom()
    dimensio.afegirIndicador("Comerç", comerç)

    # Riscos - Canviar municipis noms
    riscos = initR()
    dimensio.afegirIndicador("Riscos", riscos)

    return dimensio


def exportarUrbanistica(dimensio):
    dades = pd.DataFrame()
    i = 0
    for indicador in dimensio.dades.keys():
        dadesInd = dimensio.dades[indicador].dades
        print(indicador)
        if i == 0:
            dades = dadesInd.copy(deep=True)
        else:
            dades = pd.merge(dades, dadesInd, on=["Literal", "Any", "Codi"], how='outer')
        i += 1

    dades.to_csv(os.path.join('dades', 'resultat', "urbanistica.csv"))