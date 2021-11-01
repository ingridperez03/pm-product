from aplicacio import Aplicacio
from indicador import Indicador
from dimensio import Dimensio
from proc_demografica import initDemografica

def initApp(App):
    App = Aplicacio()
    dimensioDemografica = initDemografica()
    App.afegirDimensio("Demogràfica", dimensioDemografica)

if __name__ == "__main__":
    initApp()