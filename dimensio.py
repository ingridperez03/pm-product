import os

class Dimensio:

    def __init__(self):
        self.nom = None         # Nom de la dimensió
        self.dades = {}         # Diccionari: {Nom Indicador, Dades}
        self.numIndicadors = 0  # Quantitat indicadors

    '''
        Afegir un nou indicador a la dimensió
    '''
    def afegirIndicador(self, nom, dada):
        self.dades[nom] = dada
        self.numIndicadors += 1

    def exportarIndicador(self, nom):
        indicador = self.dades[nom]
        print(nom)
        indicador.dades.to_csv(os.path.join('dades', 'resultat', nom + ".csv"))