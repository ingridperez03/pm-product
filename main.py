from aplicacio import Aplicacio
from proc_economica import initEconomica

def initApp():
    App = Aplicacio()
    dimensioEconomica = initEconomica()
    App.afegirDimensio("Economica", dimensioEconomica)

if __name__ == "__main__":
    initApp()