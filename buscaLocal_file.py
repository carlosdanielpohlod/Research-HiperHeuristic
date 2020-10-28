from utils import *
from random import randint
class BuscaLocal:
    def __init__(self, parametros, funcaoObjetivo):
        self.parametros = parametros
        self.funcaoObjetivo = funcaoObjetivo
        self.taxaMelhora = 0
    def alterarParametros(self, parametros):
        self.parametros = parametros
    def busca(self, individuo, fluxo, distancias, indiceBuscaLocal):
        if indiceBuscaLocal == 1:
            self.buscaLocal01(individuo, fluxo, distancias)
        if indiceBuscaLocal == 2:
            self.buscaLocal02(individuo, fluxo, distancias)
        if indiceBuscaLocal == 3:
            self.subOrdenacao(individuo, fluxo, distancias)
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
    

    def buscaLocal02(self, individuo, fluxo, distancias):     


        for i in range(self.parametros.TAMCROMOSSOMO - 1):
            fitness = individuo[self.parametros.TAMCROMOSSOMO - 1]
            direitaToEsquerda = self.parametros.TAMCROMOSSOMO - 1
            for esquerdaToDireita in range(self.parametros.TAMCROMOSSOMO - 1):
                direitaToEsquerda = direitaToEsquerda - 1
                
                if direitaToEsquerda != esquerdaToDireita:
                    
                    aux = individuo[direitaToEsquerda]
                    individuo[direitaToEsquerda] = individuo[esquerdaToDireita]
                    individuo[esquerdaToDireita] = aux
                    auxilioFitness = individuo[self.parametros.TAMCROMOSSOMO - 1]
                    
                    self.funcaoObjetivo.avaliarIndividuo(individuo, fluxo, distancias)
                    
                    
                    if(individuo[self.parametros.TAMCROMOSSOMO - 1] > fitness):

                        aux2 = individuo[esquerdaToDireita]
                        individuo[esquerdaToDireita] = individuo[direitaToEsquerda]

                        
                        individuo[direitaToEsquerda] = aux2
                        individuo[self.parametros.TAMCROMOSSOMO - 1] = auxilioFitness
                        
                    else:
                        
                        
                        fitness = individuo[self.parametros.TAMCROMOSSOMO - 1]


    
    def subOrdenacao(self, individuo, fluxo, distancias):  
        indice = randint(0, self.parametros.TAMCROMOSSOMO - 4)
        # print("Antes ", individuo)   
        for i in range(self.parametros.TAMCROMOSSOMO - 2):
            if(individuo[indice + 1] > individuo[indice]):
                fitnessAnterior = individuo[self.parametros.TAMCROMOSSOMO - 1]
                aux = individuo[indice]
                individuo[indice] = individuo[indice + 1]
                individuo[indice + 1] = aux
                self.funcaoObjetivo.avaliarIndividuo(individuo, fluxo, distancias)
                if(fitnessAnterior < individuo[self.parametros.TAMCROMOSSOMO - 1]):
                    individuo[indice + 1] = individuo[indice]
                    individuo[indice] = aux
                    individuo[self.parametros.TAMCROMOSSOMO - 1] = fitnessAnterior
            while(indice + 1 == self.parametros.TAMCROMOSSOMO - 2):
                indice = randint(0, self.parametros.TAMCROMOSSOMO - 2)
            
                
        