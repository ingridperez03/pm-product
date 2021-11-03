import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

'''
    Netejar dades referents al creixement població (CP)
'''
def initCP():
    data = pd.DataFrame()
    for any in range(2000, 2021):
        nomArxiu = "CP_" + str(any)
        dataAny = pd.read_csv(nomArxiu)
        # Preprocessing necessari 
        dataAny["Any"] = any

        # Tota total 
        dataAny['Total'] = dataAny.sum(axis = 1)

        # Total per sexes 
        dataAny['Homes'] = dataAny['Homes. De 0 a 14 anys'] + dataAny['Homes. De 15 a 64 anys'] + dataAny['Homes. 65 anys o més']
        dataAny['Dones'] = dataAny['Dones. De 0 a 14 anys'] + dataAny['Dones. De 15 a 64 anys'] + dataAny['Dones. 65 anys o més']

        # Total per grups d'edat
        dataAny['0-14 Anys'] = dataAny['Homes. De 0 a 14 anys'] + dataAny['Dones. De 0 a 14 anys']
        dataAny['15-64 Anys'] = dataAny['Homes. De 15 a 64 anys'] + dataAny['Dones. De 15 a 64 anys']
        dataAny['64 o més'] = dataAny['Homes. 65 anys o més'] + dataAny['Dones. 65 anys o més']

        dataAny.drop(['Homes. De 0 a 14 anys','Dones. De 0 a 14 anys', 'Homes. De 15 a 64 anys', 
                      'Dones. De 15 a 64 anys', 'Homes. 65 anys o més', 'Dones. 65 anys o més'], axis = 1)

        data.append(dataAny)
    
    data.info()
    indicador = Indicador(data, range(2000, 2021), "municipi", "unitats")
    return indicador
        
def initDemografica():
    dimensio = Dimensio()

    # Creixement Població
    creixement = initCP()
    dimensio.afegirIndicador("Creixement Poblacio", creixement)

    return dimensio