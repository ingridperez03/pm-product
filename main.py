from aplicacio import Aplicacio
from indicador import Indicador
from dimensio import Dimensio
from proc_demografica import initDemografica
# from proc_urbanistica import initUrbanistica
# from proc_economica import initEconomica
# from proc_residencial import initResidencial

def initApp(App):
    App = Aplicacio()
    dimensioDemografica = initDemografica()
    App.afegirDimensio("Demografica", dimensioDemografica)
    # dimensioUrbanistica = initDemografica()
    # App.afegirDimensio("Urbanistica", dimensioUrbanistica)
    # dimensioEconomica = initDemografica()
    # App.afegirDimensio("Economica", dimensioEconomica)
    # dimensioResidencial = initDemografica()
    # App.afegirDimensio("Residencial", dimensioResidencial)

if __name__ == "__main__":
    initApp()