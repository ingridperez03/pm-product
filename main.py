from aplicacio import Aplicacio
from proc_urbanistica import initUrbanistica

def initApp():
    App = Aplicacio()
    dimensioUrbanistica = initUrbanistica()
    App.afegirDimensio("Urbanistica", dimensioUrbanistica)

if __name__ == "__main__":
    initApp()
