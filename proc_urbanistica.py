import os
import pandas as pd
from dimensio import Dimensio
from indicador import Indicador


data_path = os.path.join('dades','urbanistica')

'''
    Netejar dades referents als serveis (Se)
'''
def initSe():
    data = pd.DataFrame()
    path = os.path.join(data_path,'serveis')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path,nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '12_A2_SUC']]
        dataAny = dataAny.rename(columns={'NomMun':'Municipi', 'Codi_ine_6_txt':'Codi', '12_A2_SUC':'Serveis'})
        data = data.append(dataAny, ignore_index = True)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")

    return indicador


'''
    Netejar dades referents als solars (So)
'''
def initSo():
    data = pd.DataFrame()
    path = os.path.join(data_path,'solar')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path,nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '15_Qual_SUC_SISTEMES']]
        dataAny = dataAny.rename(columns={'NomMun':'Municipi', 'Codi_ine_6_txt':'Codi', '15_Qual_SUC_SISTEMES':'Solar'})
        data = data.append(dataAny, ignore_index = True)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")

    return indicador


'''
    Netejar dades referents a les zones_verdes (ZV)
'''
def initZV():
    data = pd.DataFrame()
    path = os.path.join(data_path,'zones_verdes')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path,nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '15_SV_SUC']]
        dataAny = dataAny.rename(columns={'NomMun':'Municipi', 'Codi_ine_6_txt':'Codi', '15_SV_SUC':'Zones verdes'})
        data = data.append(dataAny, ignore_index = True)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")

    return indicador


'''
    Netejar dades referents als equipaments (E)
'''
def initE():
    data = pd.DataFrame()
    path = os.path.join(data_path,'equipaments')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path,nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '20_Equip_habt']]
        dataAny = dataAny.rename(columns={'NomMun':'Municipi', 'Codi_ine_6_txt':'Codi', '20_Equip_habt':'Equipament per habitant'})
        data = data.append(dataAny, ignore_index = True)
    
    indicador = Indicador(data, range(2012, 2021), "municipi", "m2/habitant")

    return indicador


'''
    Netejar dades referents a la connectivitat (Con)
'''
def initCon():
    data = pd.DataFrame()
    path = os.path.join(data_path,'connectivitat')

    for any in range(2012, 2021):
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path,nomArxiu))
        dataAny = dataAny[['Any', 'NomMun', 'Codi_ine_6_txt', '15_SF_SUC', '15_SX1_SUC', '15_SX2_SUC']]
        dataAny = dataAny.rename(columns={'NomMun':'Municipi', 'Codi_ine_6_txt':'Codi', '15_SF_SUC':'Ferroviari', '15_SX1_SUC':'Camins Principals', '15_SX2_SUC':'Camins Secundaris'})
        data = data.append(dataAny, ignore_index = True)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")

    return indicador


'''
    Netejar dades referents al comerç
'''
def initCom():
    data = pd.DataFrame()
    path = os.path.join(data_path,'comerç')

    for any in range(2017, 2020):
        nomArxiu = "comerç_" + str(any) + ".csv"
        dataAny = pd.read_csv(os.path.join(path,nomArxiu))
        dataAny = dataAny[['Any', 'Municipi', 'Codi_ine_6_txt', 'Densitat comercial (m2 / 1.000 hab.)']]
        dataAny = dataAny.rename(columns={'NomMun':'Municipi', 'Codi_ine_6_txt':'Codi', 'Densitat comercial (m2 / 1.000 hab.)':'Densitat comercial'})
        data = data.append(dataAny, ignore_index = True)

    indicador = Indicador(data, range(2017, 2020), "municipi", "m2 / 1.000 habitants")

    return indicador



'''
    Netejar dades referents als riscos
'''
def initR():
    data = pd.DataFrame()
    path = os.path.join(data_path,'riscos')

    nomArxiu = "riscos.csv"
    dataAny = pd.read_csv(os.path.join(path,nomArxiu))
    dataAny = dataAny[['municipiNom', 'ine6', 'nivell']]
    dataAny = dataAny.rename(columns={'municipiNom':'Municipi', 'ine6':'Codi', 'nivell':'Nivell'})
    data = data.append(dataAny, ignore_index = True)

    group = data.groupby(['Municipi', 'Codi', 'Nivell'])
    data = group.size().reset_index(name='Nombre de riscos')

    indicador = Indicador(data, 2021, "municipi", "unitats")

    return indicador



def initUrbanistica():
    dimensio = Dimensio()

    serveis = initSe()
    dimensio.afegirIndicador("Serveis", serveis)

    solar = initSo()
    dimensio.afegirIndicador("Solar", solar)

    zones_verdes = initZV()
    dimensio.afegirIndicador("Zones verdes", zones_verdes)

    equipament = initE()
    dimensio.afegirIndicador("Equipament", equipament)

    connectivitat = initCon()
    dimensio.afegirIndicador("Connectivitat", connectivitat)

    comerç = initCom()
    dimensio.afegirIndicador("Comerç", comerç)

    riscos = initR()
    dimensio.afegirIndicador("Riscos", riscos)

    return dimensio