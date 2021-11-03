import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

'''
    Netejar dades referents al creixement població (CP)
'''
def initCP():
    data = pd.DataFrame()
    for any in range(2000, 2021):
        nomArxiu = "CP_" + str(any) + ".csv"
        path = "dades\\demografia\\creixement_poblacio\\"
        dataAny = pd.read_csv(path + nomArxiu, index_col=None)
        # Preprocessing necessari 
        dataAny["Any"] = any

        # Total total 
        dataAny['Total'] = dataAny['Total. De 0 a 14 anys'] + dataAny['Total. De 15 a 64 anys'] + dataAny['Total. 65 anys o més']

        # Total per sexes 
        dataAny['Homes'] = dataAny['Homes. De 0 a 14 anys'] + dataAny['Homes. De 15 a 64 anys'] + dataAny['Homes. 65 anys o més']
        dataAny['Dones'] = dataAny['Dones. De 0 a 14 anys'] + dataAny['Dones. De 15 a 64 anys'] + dataAny['Dones. 65 anys o més']

        # Total per grups d'edat
        dataAny['0-14 Anys'] = dataAny['Homes. De 0 a 14 anys'] + dataAny['Dones. De 0 a 14 anys']
        dataAny['15-64 Anys'] = dataAny['Homes. De 15 a 64 anys'] + dataAny['Dones. De 15 a 64 anys']
        dataAny['64 o més'] = dataAny['Homes. 65 anys o més'] + dataAny['Dones. 65 anys o més']

        dataAny.drop(['Homes. De 0 a 14 anys', 'Dones. De 0 a 14 anys', 'Homes. De 15 a 64 anys', 
                      'Dones. De 15 a 64 anys', 'Homes. 65 anys o més', 'Dones. 65 anys o més',
                      'Total. De 0 a 14 anys', 'Total. De 15 a 64 anys', 'Total. 65 anys o més'], axis = 1, inplace=True)

        data = data.append(dataAny)
    
    data.info()
    indicador = Indicador(data, range(2000, 2021), "municipi", "unitats")
    return indicador
        
def initDemografica():
    dimensio = Dimensio()

    # Creixement Població
    creixement = initCP()
    dimensio.afegirIndicador("Creixement Poblacio", creixement)

    return dimensio