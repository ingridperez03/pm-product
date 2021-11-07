import pandas as pd

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