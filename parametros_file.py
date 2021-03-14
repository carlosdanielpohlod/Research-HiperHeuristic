import random
class Parametros:
    
    def __init__(self):
        
        self.N = 0
        self.TAMCROMOSSOMO = self.N + 1 
        self.INFINITO = 0
        self.TAMPOPULACAO = 100
        self.MAXAVALIACOES = 91100
        self.EVMA = 0.001
        self.MAXIMAPCTBUSCA = 0.6
        self.PORCENTAGEMMUTACOES = 0  
        self.NUMMAXIMOFILHOS = 2
        self.PORCENTAGEMREPRODUCOES = 0
        self.idExecucao = 0
        self.REPRODUCAO = 1
        self.MUTACAO = 3
        self.BUSCALOCAL = 2
    def setN(self, N):
        self.N = N
        self.TAMCROMOSSOMO = self.N + 1 
        self.INFINITO = self.N + 10
    def setParametros(self, porcentagemmutacoes, numaximofilhos, porcentagemreproducoes):
        self.PORCENTAGEMMUTACOES = porcentagemmutacoes    
        self.NUMMAXIMOFILHOS = numaximofilhos
        self.PORCENTAGEMREPRODUCOES = porcentagemreproducoes

