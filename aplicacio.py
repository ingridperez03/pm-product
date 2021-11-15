import pandas as pd
from proc_demografica import exportarDemografica
from proc_urbanistica import exportarUrbanistica
from proc_economica import exportarEconomica
from proc_residencial import exportarResidencial

class Aplicacio:
    
    def __init__(self):
        self.dimensions = {}    # Diccionari: Nom Dimensio, Instancia Dimensio
    
    '''
        Afegir una nova dimensió a l'aplicació
    '''
    def afegirDimensio(self, nom, dades):
        self.dimensions[nom] = dades
        
    def exportar(self):
        for nom in self.dimensions.keys():
            dimensio = self.dimensions[nom]
            for indicador in dimensio.dades.keys():
                dimensio.exportarIndicador(indicador)
            
        exportarDemografica(self.dimensions["Demografica"])
        exportarUrbanistica(self.dimensions["Urbanistica"])
        exportarEconomica(self.dimensions["Economica"])
        exportarResidencial(self.dimensions["Residencial"])
