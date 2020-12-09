from mutacao_file import *
from utils import *
from random import *
class Reproduzir:
    def __init__(self, parametros, funcaoObjetivo, mutacao):
        self.parametros = parametros
        self.funcaoObjetivo = funcaoObjetivo
        self.score = 0
        self.mutacao = mutacao
        self.codMutacao = 0
    
    def calcularScore(self, original, perturbado):
        diferenca = ((original - perturbado)) 
        self.score = (diferenca * original) / 10000

    def reproduzir(self, populacao, fluxo, distancias, pai01, pai02, indiceReproducao):
        if(indiceReproducao == 1):
            self.reproduzir01(populacao, fluxo, distancias, pai01, pai02)
        if(indiceReproducao == 2):
            self.reproduzir02(populacao, fluxo, distancias, pai01, pai02)
        
    def aux_mutacao(self, novoIndividuo, fluxo, distancias):
        if(self.mutacao.chanceMutar()):
            
            aux = copy.deepcopy(novoIndividuo)
            self.mutacao.mutar(novoIndividuo, self.codMutacao, fluxo, distancias)
            self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
            if(aux[self.parametros.TAMCROMOSSOMO - 1] < novoIndividuo[self.parametros.TAMCROMOSSOMO - 1]):
                novoIndividuo = copy.deepcopy(aux)
                
            
        else:
            self.mutacao.score = 0
    
    def reproduzir01(self, populacao, fluxo, distancias, pai01, pai02):
       
        utils = Utils(self.parametros)
        
        escolhido = 0
        novoIndividuo = [0] * (self.parametros.TAMCROMOSSOMO)
        genePassado = 0
        listaAuxiliar = [[0 for y in range(self.parametros.TAMCROMOSSOMO)]  for x in range(self.parametros.NUMMAXIMOFILHOS + 2)]
        contadorAuxiliar = 0
        
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai01])
        
        contadorAuxiliar = contadorAuxiliar + 1 
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai02])
        
        for filho in range(self.parametros.NUMMAXIMOFILHOS):
            contadorAuxiliar = contadorAuxiliar + 1
            genePassado = 0
            escolhido = 0
            novoIndividuo = [0] * self.parametros.TAMCROMOSSOMO 
            utils.zerar(novoIndividuo)
            
        
            for i in range(self.parametros.N):
                escolhido = randint(0,1)
                genePassado = randint(0, self.parametros.TAMCROMOSSOMO - 2)
                
                if(escolhido == 0):
                
                    while(populacao[pai01][genePassado] in novoIndividuo):
                        genePassado = randint(0, self.parametros.TAMCROMOSSOMO - 2)
                        
                    novoIndividuo[i] = populacao[pai01][genePassado]
                    
                else:
                
                    while(populacao[pai02][genePassado] in novoIndividuo):
                        
                        genePassado = randint(0, self.parametros.TAMCROMOSSOMO - 2)
                        
                    novoIndividuo[i] = populacao[pai02][genePassado]
                    
                
            
            
            self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
            
            self.aux_mutacao(novoIndividuo, fluxo, distancias)
            
            utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
           
        
        
        utils.ordenar(listaAuxiliar)
        
        if(listaAuxiliar[0] != novoIndividuo): 
            self.calcularScore(listaAuxiliar[0][self.parametros.TAMCROMOSSOMO - 1], novoIndividuo[self.parametros.TAMCROMOSSOMO - 1])
           
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)

    
    def reproduzir02(self, populacao, fluxo, distancias, pai01, pai02):
        
        
        utils = Utils(self.parametros)
        numeroFilhos = randint(1, self.parametros.NUMMAXIMOFILHOS)
        maisPrivilegiado = 0
        listaAuxiliar = [[0 for y in range(self.parametros.TAMCROMOSSOMO)]  for x in range(self.parametros.NUMMAXIMOFILHOS + 2)]
        
        contadorAuxiliar = 0

        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai01])
        
        contadorAuxiliar = contadorAuxiliar + 1 
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai02])
        for filho in range(self.parametros.NUMMAXIMOFILHOS):
            contadorAuxiliar = contadorAuxiliar + 1
            if(populacao[pai01][self.parametros.TAMCROMOSSOMO - 1] < populacao[pai02][self.parametros.TAMCROMOSSOMO - 1]):
                maisPrivilegiado = pai01
                menosPrivilegiado = pai02
            else:
                maisPrivilegiado = pai02
                menosPrivilegiado = pai01 
            novoIndividuo = [self.parametros.INFINITO] * self.parametros.TAMCROMOSSOMO
            for i in range(self.parametros.TAMCROMOSSOMO):
                i = randint(0, self.parametros.TAMCROMOSSOMO - 4)
                if(i + 2 >= self.parametros.TAMCROMOSSOMO - 1):
                    i = 0
                    novoIndividuo[i] = populacao[maisPrivilegiado][i]
                else:
                    novoIndividuo[i] = populacao[maisPrivilegiado][i]
                    i = i + 2
        
            
            
            for i in range(self.parametros.TAMCROMOSSOMO):
                indice = populacao[menosPrivilegiado][i]
                
                if((indice not in novoIndividuo)and utils.posicaoVazia(novoIndividuo) != None):
                    novoIndividuo[utils.posicaoVazia(novoIndividuo)] = populacao[menosPrivilegiado][i]
           
            

            self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
            
            self.aux_mutacao(novoIndividuo, fluxo, distancias)
            
            utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
            
        utils.ordenar(listaAuxiliar)
       
        if(listaAuxiliar[0] != novoIndividuo):
            
            self.calcularScore(listaAuxiliar[0][self.parametros.TAMCROMOSSOMO - 1], novoIndividuo[self.parametros.TAMCROMOSSOMO - 1])
       
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)