from random import randint

import copy
class Mutacao:
    def __init__(self, parametros):
        self.score  = 0
        self.parametros = parametros
    
    def calcularScore(self, original, perturbado):
        diferenca = ((original - perturbado)) 
        self.score = (diferenca * original) / 10000    
    def mutar(self, individuo, codigoMutacao, fluxo, distancias):
        if(codigoMutacao == 1):
            self.mutar01(individuo, fluxo, distancias)
        if(codigoMutacao == 2):
            self.mutar02(individuo, fluxo, distancias)
        if(codigoMutacao == 3):
            self.mutar03(individuo, fluxo, distancias)
    def mutar01(self, individuo, fluxo, distancias):
        # print("Mutacao 01")
        
        copiaIndividuo = copy.deepcopy(individuo)
        N = len(individuo) - 2
        locus01 = randint(0, N)
        locus02 = randint(0, N)
        aux = 0
        while(locus01 == locus02):
            locus02 = randint(0, N)
        
        aux = individuo[locus01]
        individuo[locus01] = individuo[locus02]
        individuo[locus02] = aux
        self.calcularScore(copiaIndividuo[self.parametros.TAMCROMOSSOMO - 1], individuo[self.parametros.TAMCROMOSSOMO - 1])
        return individuo
        # print(copiaIndividuo, individuo)
    def mutar02(self, individuo, fluxo, distancias):
        
        # print("Mutação 02")
        N = len(individuo)
        copiaIndividuo = copy.deepcopy(individuo)
        pivo = randint(2, N - 3)
        valor = randint(1, N - 2)
        while(valor == pivo):
            valor = randint(1, N - 2)
        aux = individuo[pivo - 1]
        individuo[pivo - 1] = individuo[valor]
        individuo[valor] = aux
        self.calcularScore(copiaIndividuo[self.parametros.TAMCROMOSSOMO - 1], individuo[self.parametros.TAMCROMOSSOMO - 1])
        return individuo
        
    def mutar03(self, individuo, fluxo, distancias):
        
        copiaIndividuo = copy.deepcopy(individuo)
        N = len(individuo)
        pivo = randint(2, N - 2)
        subCadeia = [individuo[pivo], individuo[pivo - 1], individuo[pivo - 2]]
        sorted(subCadeia)
        individuo[pivo - 2] = subCadeia[0]
        individuo[pivo - 1] = subCadeia[1]
        individuo[pivo] = subCadeia[2]
        self.calcularScore(copiaIndividuo[self.parametros.TAMCROMOSSOMO - 1], individuo[self.parametros.TAMCROMOSSOMO - 1])
        return individuo
    def chanceMutar(self):
       
        mutar = randint(0, 100)
        if(mutar <= self.parametros.PORCENTAGEMMUTACOES):
            
            return True
        else:
            
            return False
    
