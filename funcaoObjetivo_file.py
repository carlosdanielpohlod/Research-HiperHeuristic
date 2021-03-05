from random import randint
from utils import *

class FuncaoObjetivo:
    def __init__(self, parametros):
        self.parametros = parametros
        self.utils = Utils(parametros)
    def setParametros(self, parametros):
        self.parametros = parametros
      
    def gerarPopulacao(self, populacao):
        self.parametros.N 

        novoIndividuo = [0] * self.parametros.TAMCROMOSSOMO  
        existe = False
        num = 0
        individuo = 0  
        locus = 0

        for individuo in range(self.parametros.TAMPOPULACAO):
            self.utils.zerar(novoIndividuo)
            # novoIndividuo =  [self.parametros.TAMCROMOSSOMO + 3] *len(novoIndividuo) *
            while(locus < self.parametros.N):
                

                num = randint(0,self.parametros.N - 1)
                existe = False

                for i in range(self.parametros.TAMCROMOSSOMO - 1):
                    
                    if(novoIndividuo[i] == num):
                        
                        existe = True
                        break
                    
                    
                
                if(existe == False):              
                    novoIndividuo[locus] = num   
                    locus = locus + 1  
            
            locus = 0
            
            for j in range(self.parametros.TAMCROMOSSOMO - 1):
                
                # print(novoIndividuo[j])
                populacao[individuo][j] = novoIndividuo[j]
            
            populacao[individuo][self.parametros.TAMCROMOSSOMO - 1] = 0
        
    def avaliarIndividuo(self,individuo, fluxo, distancias):
        
        fitness = 0
        
        for i in range(self.parametros.N):
            for j in range(self.parametros.N):
                
                fitness = fitness + distancias[i][j] * fluxo[ individuo[i] ] [individuo[j] ]
    
        individuo[self.parametros.TAMCROMOSSOMO - 1] = fitness
        
    
    def avaliarPopulacao(self, populacao, fluxo, distancias):
        for individuo in range(self.parametros.TAMPOPULACAO):
            
            self.avaliarIndividuo(populacao[individuo], fluxo, distancias)
    