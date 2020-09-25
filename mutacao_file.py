from random import randint
class Mutacao:

    def mutar(self, individuo, codigoMutacao):
        if(codigoMutacao == 1):
            self.mutar01(individuo)

    def mutar01(self, individuo):
        N = len(individuo) - 1
        locus01 = randint(0, N)
        locus02 = randint(0, N)
        aux = 0
        while(locus01 == locus02):
            locus02 = randint(0, N)
        
        aux = individuo[locus01]
        individuo[locus01] = individuo[locus02]
        individuo[locus02] = aux

    def chanceMutar(self, PORCENTAGEMMUTACOES):
       
        mutar = randint(0, 100)
        if(mutar <= PORCENTAGEMMUTACOES):
            
            return True
        else:
            
            return False
    
