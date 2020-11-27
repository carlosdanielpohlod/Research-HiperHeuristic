from operator import itemgetter
from random import *
from codHeuristicas import CodHeuristicas
class Utils:
    def __init__(self, parametros = None):
        self.parametros = parametros
    def inserir(self, individuoCopia, individuoCopiado):
        for i in range(self.parametros.TAMCROMOSSOMO):
            individuoCopia[i] = individuoCopiado[i]
    def zerar(self, individuo):
        for i in range(self.parametros.TAMCROMOSSOMO):
            individuo[i] = self.parametros.INFINITO
        
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
    def declararMatriz(self, linhas, colunas):
        return [[0 for x in range(colunas)] for y in range(linhas)]
    def posicaoVazia(self, individuo):
        for i in range(self.parametros.TAMCROMOSSOMO - 1):
            if individuo[i] == self.parametros.INFINITO:
                return i
        return None
    def existe(self, gene, individuo02):
        for i in range(self.parametros.TAMCROMOSSOMO - 1):
            
            if gene == individuo02[i]:
                return True
        return False
    def printMatriz(self, matriz):
        
        for i in range(len(matriz)):
            print(matriz[i])
    def codToString(self, codHeuristicas):
        return f'{codHeuristicas.codReproducao},{codHeuristicas.codBuscaLocal},{codHeuristicas.codSelecaoPais}'
    def castArray(self, array):
        array = array.split(',')
        for i in range(len(array)):
            array[i] = int(array[i])
        return array

    def setCodigosHeuriticas(self, codHeuristicas, codigos):
        if(codigos == 'random'):
           
            codHeuristicas.codReproducao, codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais =  [randint(1,2), randint(1,3), randint(1,2)]
        else:
            codigos = self.castArray(codigos)
            codHeuristicas.codReproducao, codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais = codigos
            
    def ordenar(self,matriz):
        aux = [0] * self.parametros.TAMCROMOSSOMO
        # tamMatriz = len(matri)
        for j in range(self.parametros.NUMMAXIMOFILHOS):
            for i in range(self.parametros.NUMMAXIMOFILHOS + 1):

                if(matriz[i][self.parametros.TAMCROMOSSOMO - 1] > matriz[i + 1][self.parametros.TAMCROMOSSOMO - 1] ):
                    for k in range (self.parametros.TAMCROMOSSOMO):
                        
                        aux[k] = matriz[i][k]
                    
                    for k in range(self.parametros.TAMCROMOSSOMO):
                        matriz[i][k] = matriz[i + 1][k]
                    
                    for k in range(self.parametros.TAMCROMOSSOMO):
                        matriz[i + 1][k] = aux[k]
    def bubbleSort(self, matriz):
        aux = [self.parametros.INFINITO] * self.parametros.TAMCROMOSSOMO
        
        for j in range(self.parametros.TAMPOPULACAO):
            for i in range(self.parametros.TAMPOPULACAO - 1):

                if(matriz[i][self.parametros.TAMCROMOSSOMO - 1] > matriz[i + 1][self.parametros.TAMCROMOSSOMO - 1] ):
                    for k in range (self.parametros.TAMCROMOSSOMO):
                        
                        aux[k] = matriz[i][k]
                    
                    for k in range(self.parametros.TAMCROMOSSOMO):
                        matriz[i][k] = matriz[i + 1][k]
                    
                    for k in range(self.parametros.TAMCROMOSSOMO):
                        matriz[i + 1][k] = aux[k]     
    