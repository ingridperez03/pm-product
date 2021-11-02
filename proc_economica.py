import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

'''
    Netejar dades referents al creixement població
'''
def initCP():
    data = pd.DataFrame()
    for any in range(2000, 2021):
        nomArxiu = "CP_" + str(any)
        dataAny = pd.read_csv(nomArxiu)
        # Preprocessing necessari
        dataAny["Any"] = any
        data.append(dataAny)
    
    data.info()
    indicador = Indicador(data, range(2000, 2021), "municipi", "unitats")
    return indicador
        
def initDemografica():
    dimensio = Dimensio()

    # Creixement Població
    creixement = initCP()
    dimensio.afegirIndicador("Creixement Població", creixement)

    return dimensio