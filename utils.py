from operator import itemgetter
class Utils:
    def __init__(self, parametros):
        self.parametros = parametros
    def inserir(self, individuoCopia, individuoCopiado):
        for i in range(self.parametros.TAMCROMOSSOMO):
            individuoCopia[i] = individuoCopiado[i]
    def zerar(self, individuo):
        for i in range(len(individuo)):
            individuo[i] = self.parametros.TAMCROMOSSOMO + 3
    def persistirMelhores(self, matriz, populacao,  pai01,  pai02):
        for i in range(self.parametros.TAMCROMOSSOMO):
        
            populacao[pai01][i] = matriz[0][i]
            populacao[pai02][i] = matriz[1][i]
    def buscarMelhorIndividuo(self, populacao):
        melhor = 0
        for i in range(self.parametros.TAMPOPULACAO):
            if(populacao[i][self.parametros.TAMCROMOSSOMO - 1] < populacao[melhor][self.parametros.TAMCROMOSSOMO - 1]):
                melhor = i
        return melhor
    def ordenar(self,matriz):
            aux = [0] * self.parametros.TAMCROMOSSOMO
            
            for j in range(self.parametros.NUMMAXIMOFILHOS):
                for i in range(self.parametros.NUMMAXIMOFILHOS + 1):

                    if(matriz[i][self.parametros.TAMCROMOSSOMO - 1] > matriz[i + 1][self.parametros.TAMCROMOSSOMO - 1] ):
                        for k in range (self.parametros.TAMCROMOSSOMO):
                            
                            aux[k] = matriz[i][k]
                        
                        for k in range(self.parametros.TAMCROMOSSOMO):
                            matriz[i][k] = matriz[i + 1][k]
                        
                        for k in range(self.parametros.TAMCROMOSSOMO):
                            matriz[i + 1][k] = aux[k]
                
    