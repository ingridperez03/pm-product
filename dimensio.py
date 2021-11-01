class Dimensio:

    def __init__(self):
        self.nom = None         # Nom de la dimensió
        self.dades = {}         # Diccionari: {Nom Indicador, Dades}
        self.numIndicadors = 0  # Quantitat indicadors

    def afegirIndicador(self, nom, dada):
        self.dades[nom] = dada
        self.numIndicadors += 1
