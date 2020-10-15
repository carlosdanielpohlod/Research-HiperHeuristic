from utils import *
class BuscaLocal:
    def __init__(self, parametros, funcaoObjetivo):
        self.parametros = parametros
        self.funcaoObjetivo = funcaoObjetivo
    def alterarParametros(self, parametros):
        self.parametros = parametros
    def busca(self, individuo, fluxo, distancias, indiceReproducao):
        if indiceReproducao == 1:
            self.buscaLocal01(individuo, fluxo, distancias)
    # def buscaLocal02(self, individuo, fluxi, distancias):

    def buscaLocal01(self, individuo, fluxo, distancias):        
        for i in range(self.parametros.TAMCROMOSSOMO - 1):
            fitness = individuo[self.parametros.TAMCROMOSSOMO - 1]

            for j in range(self.parametros.TAMCROMOSSOMO - 1):
                if i != j:
                    aux = individuo[i]
                    individuo[i] = individuo[j]
                    individuo[j] = aux
                    auxilioFitness = individuo[self.parametros.TAMCROMOSSOMO - 1]

                    self.funcaoObjetivo.avaliarIndividuo(individuo, fluxo, distancias)

                    if(individuo[self.parametros.TAMCROMOSSOMO - 1] > fitness):
                        aux2 = individuo[j]
                        individuo[j] = individuo[i]

                        
                        individuo[i] = aux2
                        individuo[self.parametros.TAMCROMOSSOMO - 1] = auxilioFitness
                        
                    else:
                        fitness = individuo[self.parametros.TAMCROMOSSOMO - 1]
    

