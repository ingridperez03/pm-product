class Indicador:

    def __init__(self, dades, anys, nivell, unitats):
        self.dades = dades       # Pandas dataframe
        self.anys = anys          # 2000 - 2020 
        self.nivell = nivell      # Nivell catalunya, província, comarca, municipi
        self.unitats = unitats     # milions, milers, unitats
    