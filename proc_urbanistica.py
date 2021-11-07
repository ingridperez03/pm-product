import os
import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

# Path localització dades urbanistiques
data_path = os.path.join('dades', 'urbanistica')

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
        dataAny.rename(columns={'NomMun':'Literal', 'Codi_ine_6_txt':'Codi', '12_A2_SUC':'Serveis'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")
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
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '15_Qual_SUC_SISTEMES']]
        dataAny.rename(columns={'NomMun':'Literal', 'Codi_ine_6_txt':'Codi', '15_Qual_SUC_SISTEMES':'Solar'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)
    
    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")
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
        dataAny.rename(columns={'NomMun':'Literal', 'Codi_ine_6_txt':'Codi', '15_SV_SUC':'Zones verdes'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")
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
        dataAny.rename(columns={'NomMun':'Literal', 'Codi_ine_6_txt':'Codi', '20_Equip_habt':'Equipament'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)
 
    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2012, 2021), "municipi", "m2 / habitant")
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
        dataAny.rename(columns={'NomMun':'Literal', 'Codi_ine_6_txt':'Codi', '15_SF_SUC':'Ferroviari', '15_SX1_SUC':'Camins Principals', '15_SX2_SUC':'Camins Secundaris'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data["Connectivitat"] = data[["Ferroviari", "Camins Principals", "Camins Secundaris"]].sum(axis=1)
    data.drop(["Ferroviari", "Camins Principals", "Camins Secundaris"], axis=1, inplace=True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")
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
        dataAny.rename(columns={'NomMun':'Literal', 'Codi_ine_6_txt':'Codi', 'Densitat comercial (m2 / 1.000 hab.)':'Densitat comercial'}, inplace=True)
        data = data.append(dataAny, ignore_index = True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, range(2017, 2020), "municipi", "m2 / 1.000 habitants")
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
    dataAny = dataAny.rename(columns={'municipiNom':'Literal', 'ine6':'Codi', 'nivell':'Nivell'})
    data = data.append(dataAny, ignore_index = True)

    group = data.groupby(['Literal', 'Codi'])
    data = group.size().reset_index(name='Riscos')

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, 2021, "municipi", "unitats")
    return indicador


def initUrbanistica():
    dimensio = Dimensio()

    # Serveis
    serveis = initSe()
    dimensio.afegirIndicador("Serveis", serveis)

    # Solar
    solar = initSo()
    dimensio.afegirIndicador("Solar", solar)

    # Zones verdes
    zones_verdes = initZV()
    dimensio.afegirIndicador("Zones verdes", zones_verdes)

    # Equipaments
    equipament = initE()
    dimensio.afegirIndicador("Equipament", equipament)

    # Connectivitat
    connectivitat = initCon()
    dimensio.afegirIndicador("Connectivitat", connectivitat)

    # Comerç
    comerç = initCom()
    dimensio.afegirIndicador("Comerç", comerç)

    # Riscos
    riscos = initR()
    dimensio.afegirIndicador("Riscos", riscos)

    return dimensio