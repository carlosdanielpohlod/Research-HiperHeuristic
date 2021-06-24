from random import randint
from utils import *

class FuncaoObjetivo:
    def __init__(self, parametros):
        self.parametros = parametros
        self.utils = Utils(parametros)
    def setParametros(self, parametros):
        self.parametros = parametros
      
    def gerarPopulacao(self, populacao):
       
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
                
                
                populacao[individuo][j] = novoIndividuo[j]
            
            populacao[individuo][self.parametros.TAMCROMOSSOMO - 1] = self.parametros.INFINITO
        
    def avaliarIndividuo(self,individuo, fluxo, distancias):
        
        fitness = 0
        self.utils.infactivelCheck(individuo)
        for i in range(self.parametros.N):
            for j in range(self.parametros.N):
                
                fitness = fitness + distancias[i][j] * fluxo[ individuo[i] ] [individuo[j] ]
    
        individuo[self.parametros.TAMCROMOSSOMO - 1] = fitness
        
    def infactivelCheck(self,fluxo, distancias,individuo, instancia):
        
    
        individuo = individuo
        instancia = instancia.split("/")[-1]
        
        bestInstancia = dict([
            ('nug12.dat',	578),
            ('nug14.dat',	1016),
            ('nug15.dat',	1150),
            ('nug16a.dat',	1612),
            ('nug16b.dat',	1610),
            ('nug17.dat',	1732),
            ('nug18.dat',	1948),
            ('nug20.dat',	2570),
            ('nug21.dat',	2450),
            ('nug22.dat',	3596),
            ('nug25.dat',	3744),
            ('nug27.dat',	5264),
            ('nug28.dat',	518),
        ])
        self.avaliarIndividuo(individuo, fluxo, distancias)
        
        if(individuo[self.parametros.TAMCROMOSSOMO - 1] < int(bestInstancia[instancia])):
            print(f'indivi infactivel {individuo}, best: {bestInstancia[instancia]}, instancia: {instancia}')


        for i in range(len(individuo) - 1):
            val = individuo[i]
            for j in range(len(individuo) - i):
                if(i != j and individuo[j] == val):
                    print("Infactivel -> ", individuo[j], 'repetiu em ', individuo)     
                    return 
    def avaliarPopulacao(self, populacao, fluxo, distancias):
        for individuo in range(self.parametros.TAMPOPULACAO):
            
            self.avaliarIndividuo(populacao[individuo], fluxo, distancias)
    