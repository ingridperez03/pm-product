class Aplicacio:
    
    def __init__(self):
        self.dimensions = {}    # Diccionari: Nom Dimensio, Instancia Dimensio
    
    '''
        Afegir una nova dimensió a l'aplicació
    '''
    def afegirDimensio(self, nom, dades):
        self.dimensions[nom] = dades
        