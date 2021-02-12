class CodHeuristicas:
    
    def __init__(self):
        self.codReproducao = 0
        self.codBuscaLocal = 0
        self.codSelecaoPais = 0
        self.codMutacao = 0
        self.fitness = 0

        self.qtdReproducao = 2
        self.qtdBuscaLocal = 3
        self.qtdMutacao = 3