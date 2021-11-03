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
    print(data)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")

    return indicador


def initUrbanistica():
    dimensio = Dimensio()

    serveis = initSe()
    dimensio.afegirIndicador("Serveis", serveis)

    return dimensio