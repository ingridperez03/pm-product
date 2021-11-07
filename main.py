from aplicacio import Aplicacio
from proc_demografica import initDemografica
from proc_urbanistica import initUrbanistica
from proc_economica import initEconomica
from proc_residencial import initResidencial

def initApp():
    App = Aplicacio()
    
    # Dimensio demografica
    dimensioDemografica = initDemografica()
    App.afegirDimensio("Demografica", dimensioDemografica)
    
    # Dimensio urbanistica
    dimensioUrbanistica = initUrbanistica()
    App.afegirDimensio("Urbanistica", dimensioUrbanistica)
    
    # Dimensio Economica
    dimensioEconomica = initEconomica()
    App.afegirDimensio("Economica", dimensioEconomica)
    
    # Dimensio Residencial
    dimensioResidencial = initResidencial()
    App.afegirDimensio("Residencial", dimensioResidencial)

if __name__ == "__main__":
    initApp()
