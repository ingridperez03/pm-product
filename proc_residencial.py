import os
import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

data_path = os.path.join('dades', 'residencials')
municipis = pd.read_csv(os.path.join('dades', 'noms_municipis.csv'))

'''
    Netejar dades referents a l'any de creació dels edificis (antiguitat)
'''
def initAC():
    path = os.path.join(data_path, 'any_construccio')

    nom_arxiu = 'AC_2011.csv'
    data = pd.read_csv(os.path.join(path, nom_arxiu), index_col=False)
    data.drop(columns="Total", inplace=True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)

    rang = ["Abans de 1900", "De 1900 a 1920", "De 1921 a 1940", "De 1941 a 1950", "De 1951 a 1960", 
            "De 1961 a 1970", "De 1971 a 1980", "De 1981 a 1990", "De 1991 a 2001", "De 2002 a 2011"]
    indicador = Indicador(data, rang, 'municipi', 'habitatges construits')
    return indicador


'''
    Netejar dades referents a la demanda de habitatges socials per anys (demanda)
'''
def initDem():
    path = os.path.join(data_path, 'demanda')

    nom_arxiu = 'DHS_2020.csv'
    data = pd.read_csv(os.path.join(path, nom_arxiu), index_col=False)
    data.drop(columns="Codi", inplace=True)
    data = pd.merge(data, municipis, left_on="Literal", right_on="Municipi")
    data.drop(columns=["NomMun", "Municipi"], inplace=True)

    data = data.melt(id_vars=["Literal", "Codi"], var_name="Any", value_name="Demanda")
    data = data[data["Demanda"] != "-"]
    data.reset_index(inplace=True)
    data["Demanda"] = data["Demanda"].astype(int)
    data.drop(columns="index", inplace=True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)
    data["Any"] = data["Any"].astype(int)

    indicador = Indicador(data, range(2011, 2021), 'municipi', 'habitatges solicitats')
    return indicador


'''
    Netejar dades referents als habitants que viuen en un habitatge (PH)
'''
def initPH():
    path = os.path.join(data_path, 'persones_habitatge')
    
    data = pd.DataFrame()
    for any in [2001, 2011]:
        nom_arxiu = 'PH_' + str(any) + '.csv'
        dataAny = pd.read_csv(os.path.join(path,nom_arxiu))
        dataAny['Any'] = any
        
        if any == 2001:
            dataAny[">6"] += dataAny["6"]
            dataAny.drop(columns="6", inplace=True)
        
        dataAny["Codi"] = range(1, dataAny.shape[0] + 1)
        dataAny["Codi"] = dataAny["Codi"].astype(str).str.zfill(2)
        
        data = data.append(dataAny)

    data.rename(columns={">6": ">=6"}, inplace=True)
    data.drop(columns="Total", inplace=True)

    indicador = Indicador(data, [2001, 2011], 'comarca', 'persones per habitatge')
    return indicador


'''
    Netejar dades referents als tipus d'habitatges (TH)
'''
def initTH():
    path = os.path.join(data_path, 'tipus')

    data = pd.DataFrame()
    for any in [2001, 2011]:
        nom_arxiu = 'TH_' + str(any) + '.csv'
        dataAny = pd.read_csv(os.path.join(path,nom_arxiu))
        dataAny['Any'] = any

        if any == 2001:
            dataAny["Habitatges familiars principals"] = dataAny["Habitatges familiars  principals  convencionals"] + dataAny["Habitatges familiars  principals  allotjaments"]
            dataAny.rename(columns = {"Habitatges familiars  no principals  secundaris": "Habitatges familiars secundaris", 
                                      "Habitatges familiars  no principals  vacants": "Habitatges familiars vacants", 
                                      "Habitatges familiars  no principals  altres": "Habitatges familiars altres"}, inplace=True)

            dataAny.drop(columns=["Habitatges familiars  principals  convencionals", "Habitatges familiars  principals  allotjaments", "Habitatges familiars    total", "Establiments col·lectius"], inplace=True)

        elif any == 2011:
            dataAny.rename(columns = {"Habitatges familiars    principals": "Habitatges familiars principals", "Habitatges familiars  no principals  secundaris": "Habitatges familiars secundaris", 
                            "Habitatges familiars  no principals  buits": "Habitatges familiars vacants"}, inplace=True)

            dataAny.drop(columns=[ "Habitatges familiars  no principals  total", "Habitatges familiars    total", "Habitatges col·lectius"], inplace=True)

        data = data.append(dataAny)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)

    indicador = Indicador(data, [2001, 2011], 'municipi', 'nombre habitatges')
    return indicador


'''
    Netejar dades referents al règim de tinença (RT)
'''
def initRT():
    path = os.path.join(data_path, 'tinença')

    data = pd.DataFrame()
    for any in [2001, 2011]:
        nom_arxiu = 'RT_' + str(any) + '.csv'
        dataAny = pd.read_csv(os.path.join(path, nom_arxiu))
        dataAny['Any'] = any

        dataAny["De propietat"] = dataAny["De propietat. Per compra pagada"] + dataAny["De propietat. Per compra amb pagaments pendents"] + dataAny["De propietat. Per herència o donació"]
        
        dataAny.drop(columns=["De propietat. Per compra pagada","De propietat. Per compra amb pagaments pendents","De propietat. Per herència o donació","Cedit gratis o a baix preu","Altres formes","Total"], inplace=True)
        data = data.append(dataAny)
    
    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)

    indicador = Indicador(data, [2001, 2011], 'municipi', 'nombre habitatges')
    return indicador


def initResidencial():

    dimensio = Dimensio()

    # Antiguitat 
    any_construccio = initAC() 
    dimensio.afegirIndicador('Edificis per any construccio', any_construccio)

    # Demanda
    demanda = initDem()
    dimensio.afegirIndicador('Demanda Social', demanda)

    # Habitants per habitatge 
    habitants = initPH()
    dimensio.afegirIndicador('Habitants per Habitatge', habitants)

    # Tipus Habitatges 
    tipus = initTH()
    dimensio.afegirIndicador('Tipus Habitatges', tipus)

    # Regim de Tinença
    tinença = initRT()
    dimensio.afegirIndicador('Regim de Tinença', tinença)
    
    return dimensio


def exportarResidencial(dimensio):
    dades = pd.DataFrame()
    i = 0
    for indicador in dimensio.dades.keys():
        dadesInd = dimensio.dades[indicador].dades

        if indicador == "Edificis per any construccio":
            dadesInd.to_csv(os.path.join('dades', 'resultat', "residencial_antiguitat.csv"))

        elif indicador == "Habitants per Habitatge":
            dadesInd.to_csv(os.path.join('dades', 'resultat', "residencial_comarcal.csv"))
            
        else: 
            if i == 0:
                dades = dadesInd.copy(deep=True)
            else:
                dades = pd.merge(dades, dadesInd, on=["Literal", "Any", "Codi"], how='outer')
            i += 1
            dades.to_csv(os.path.join('dades', 'resultat', "residencial.csv"))