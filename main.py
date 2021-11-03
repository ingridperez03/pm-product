from aplicacio import Aplicacio
from indicador import Indicador
from dimensio import Dimensio
from proc_serveis import initUrbanistica

def initApp():
    App = Aplicacio()
    dimensioUrbanistica = initUrbanistica()
    App.afegirDimensio("Urbanística", dimensioUrbanistica)
    print(App.dimensions)

if __name__ == "__main__":
    initApp()