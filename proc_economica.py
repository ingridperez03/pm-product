import pandas as pd
from dimensio import Dimensio
from indicador import Indicador
import os

data_path = os.path.join('dades', 'economiques')
municipis = pd.read_csv(os.path.join('dades', 'noms_municipis.csv'))

'''
    Netejar dades referents  al atur per any
'''
def initAtur():
    data = pd.read_csv(os.path.join(data_path, 'Atur', 'aturats_catalunya_12-20.csv'))
    data.rename(columns={"Municipi": "Literal"}, inplace=True)
    
    data = data.melt(id_vars =["Literal", "Codi"], var_name="Any", value_name="Aturats")

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)
    
    indicador = Indicador(data, list(range(2012, 2021)), "municipi", "unitats")
    return indicador


def initEvAtur():
    data = pd.read_csv(os.path.join(data_path, 'EvolucioAtur', 'evolucio_atur_12-20.csv'), index_col="Index")
    data.rename(columns={"Municipi": "Literal"}, inplace=True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(int).astype(str).str.zfill(6)
    
    indicador = Indicador(data, list(range(2012, 2021)), "municipi", "unitats")
    return indicador


def initPobAct():
    data = pd.read_csv(os.path.join(data_path, 'PoblacioActiva', 'poblacio_activa_2011.csv'))
    data = pd.merge(data, municipis, on="Municipi")
    data.drop(columns="NomMun", inplace=True)
    data.rename(columns={"Municipi": "Literal", "Total": "Poblacio activa"}, inplace=True)

    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, list([2011]), "municipi", "unitats")
    return indicador


def initRFDB():
    data = pd.read_csv(os.path.join(data_path, 'RendaFamiliar', 'RFDB_evolucio_2010_2018.csv'))
    data = pd.merge(data, municipis, on="Municipi")
    data.drop(columns="NomMun", inplace=True)
    data.rename(columns={"Municipi": "Literal"}, inplace=True)

    data = data.melt(id_vars =["Literal", "Codi"], var_name="Any", value_name="Renda")
    
    data = data[data["Codi"].notna()]
    data["Codi"] = data["Codi"].astype(str).str.zfill(6)

    indicador = Indicador(data, list(range(2010, 2019)), "municipi amb mes de mil habitants", "milers")
    return indicador


def initEconomica():
    dimensio = Dimensio()

    # Mitjana aturats per any i municipi
    aturats = initAtur()
    dimensio.afegirIndicador("Aturats per any", aturats)

    # Afegir evolucio de l'atur
    ev_atur = initEvAtur()
    dimensio.afegirIndicador("Evolucio de l'atur", ev_atur)

    # Afegir poblacio activa, del estudi del 2011
    pob_activa = initPobAct()
    dimensio.afegirIndicador("Poblacio activa l'any 2011", pob_activa)

    # Afegir Renda Bruta per Habitant
    renta_habitant = initRFDB()
    dimensio.afegirIndicador('Renda per Habitant', renta_habitant)

    return dimensio

