from aplicacio import Aplicacio
from indicador import Indicador
from dimensio import Dimensio
from proc_residencial import initResidencial

def initApp():
    App = Aplicacio()
    dimensioResidencial = initResidencial()
    App.afegirDimensio("Residencial", dimensioResidencial)

if __name__ == "__main__":
    initApp()