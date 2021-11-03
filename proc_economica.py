import pandas as pd
from dimensio import Dimensio
from indicador import Indicador
import os
'''
    Netejar dades referents  al atur per any
'''
data_path = os.path.join('dades','economiques')
def initAtur():
    data = pd.read_csv(os.path.join(data_path,'Atur','aturats_catalunya_12-20.csv'))
    
    indicador = Indicador(data, range(2012, 2020), "municipi", "unitats")
    return indicador
        
def initEconomica():
    dimensio = Dimensio()

    # Mitjana aturats per any i municipi
    aturats = initAtur()
    dimensio.afegirIndicador("Aturats per any", aturats)

    return dimensio

