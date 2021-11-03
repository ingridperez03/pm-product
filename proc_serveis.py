import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

'''
    Netejar dades referents als serveis
'''
def initCP():
    data = pd.DataFrame()
    
    for any in range(2012, 2021):
        path = "C://Users/david/Documents/GitHub/pm-product/dades/urbanistica/serveis/"
        nomArxiu = "dades_mapa_" + str(any) + ".csv"
        dataAny = pd.read_csv(path + nomArxiu)
        dataServeis = dataAny[['Any', 'NomMun', '12_A2_SUC']]
        data = data.append(dataServeis, ignore_index = True)

    indicador = Indicador(data, range(2012, 2021), "municipi", "Ha")

    return indicador

        
def initUrbanistica():
    dimensio = Dimensio()

    # Serveis
    serveis = initCP()
    dimensio.afegirIndicador("Serveis", serveis)

    return dimensio