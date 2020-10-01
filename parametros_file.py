import random
class Parametros:
    
    def __init__(self ):
        self.N = 12
        self.TAMCROMOSSOMO = self.N + 1
        
        self.TAMPOPULACAO = 100
        self.MAXAVALIACOES = 91100
        self.EVMA = 0.001
        self.MAXIMAPCTBUSCA = 0.6
        self.PORCENTAGEMMUTACOES = 0   
        self.NUMMAXIMOFILHOS = 0
        self.PORCENTAGEMREPRODUCOES = 0


    def setParametros(self, porcentagemmutacoes, numaximofilhos, porcentagemreproducoes):
        self.PORCENTAGEMMUTACOES = porcentagemmutacoes    
        self.NUMMAXIMOFILHOS = numaximofilhos
        self.PORCENTAGEMREPRODUCOES = porcentagemreproducoes

