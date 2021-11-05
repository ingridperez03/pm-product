import pandas as pd
from dimensio import Dimensio
from indicador import Indicador
import os
'''
    Netejar dades referents  al atur per any
'''

data_path = os.path.join('dades', 'economiques')


def initAtur():
    data = pd.read_csv(os.path.join(data_path,
                                    'Atur',
                                    'aturats_catalunya_12-20.csv'))

    indicador = Indicador(data, list(range(2012, 2021)), "municipi", "unitats")

    return indicador


def initEvAtur():
    data = pd.read_csv(os.path.join(data_path,
                                    'EvolucioAtur',
                                    'evolucio_atur_12-20.csv'))

    indicador = Indicador(data, list(range(2012, 2021)), "municipi", "unitats")

    return indicador


def initPobAct():
    data = pd.read_csv(os.path.join(data_path,
                                    'PoblacioActiva',
                                    'poblacio_activa_2011.csv'))

    indicador = Indicador(data, list(2011), "municipi", "unitats")

    return indicador


def initRFDB():
    data = pd.read_csv(os.path.join(data_path,
                                    'RendaFamiliar',
                                    'RFDB_evoluci�_2010_2018.csv'))

    indicador = Indicador(data,
                          list(range(2010, 2019)),
                          "municipi amb m�s de mil habitants",
                          "milers")

    return indicador


def initEconomica():
    dimensio = Dimensio()

    # Mitjana aturats per any i municipi
    aturats = initAtur()
    dimensio.afegirIndicador("Aturats per any", aturats)

    # Afegir evoluci� de l'atur
    ev_atur = initEvAtur()
    dimensio.afegirIndicador("Evoluci� de l'atur", ev_atur)

    # Afegir poblaci� activa, del estudi del 2011
    pob_activa = initPobAct()
    dimensio.afegirIndicador("Poblaci� activa l'any 2011", pob_activa)

    # Afegir Renda Bruta per Habitant
    renta_habitant = initRFDB()
    dimensio.afegirIndicador('Renda per Habitant', renta_habitant)

    return dimensio

