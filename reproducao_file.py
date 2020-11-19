from mutacao_file import *
from utils import *
from random import *
class Reproduzir:
    def __init__(self, parametros, funcaoObjetivo):
        self.parametros = parametros
        self.funcaoObjetivo = funcaoObjetivo
        self.score = 0
    # def calcularScore(self, anterior, novo):
    def calcularScore(self, original, perturbado):
        diferenca = ((original - perturbado)) 
        self.score = (diferenca * original) / 10000

    def reproduzir(self, populacao, fluxo, distancias, pai01, pai02, indiceReproducao):
        if(indiceReproducao == 1):
            self.reproduzir01(populacao, fluxo, distancias, pai01, pai02)
        if(indiceReproducao == 2):
            self.reproduzir02(populacao, fluxo, distancias, pai01, pai02)
        


    def reproduzir01(self, populacao, fluxo, distancias, pai01, pai02):
        # listaAuxiliar[0][self.parametros.TAMCROMOSSOMO - 1] = (populacao[pai01][self.parametros.TAMCROMOSSOMO - 1] + populacao[pai02][self.parametros.TAMCROMOSSOMO - 1]) / 2
        utils = Utils(self.parametros)
        mutacao = Mutacao()
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
                    
                
            
            if(mutacao.chanceMutar(self.parametros.PORCENTAGEMMUTACOES)):
                mutacao.mutar(novoIndividuo, 1)
            
            self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)

            utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
           
        
        
        utils.ordenar(listaAuxiliar)
        print(listaAuxiliar)
        if(listaAuxiliar[0] != novoIndividuo): 
            self.calcularScore(listaAuxiliar[0][self.parametros.TAMCROMOSSOMO - 1], novoIndividuo[self.parametros.TAMCROMOSSOMO - 1])
           
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)

    
    def reproduzir02(self, populacao, fluxo, distancias, pai01, pai02):
        # listaAuxiliar[0][self.parametros.TAMCROMOSSOMO - 1] = (populacao[pai01][self.parametros.TAMCROMOSSOMO - 1] + populacao[pai02][self.parametros.TAMCROMOSSOMO - 1]) / 2
        # print(populacao[pai01], populacao[pai02],"\n")
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
            # print("filho ", novoIndividuo)
            

            self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
            utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
        utils.ordenar(listaAuxiliar)
        # print(listaAuxiliar)
        if(listaAuxiliar[0] != novoIndividuo):
            
            self.calcularScore(listaAuxiliar[0][self.parametros.TAMCROMOSSOMO - 1], novoIndividuo[self.parametros.TAMCROMOSSOMO - 1])
            # if(novoIndividuo[self.parametros.TAMCROMOSSOMO - 1] > listaAuxiliar[0][self.parametros.TAMCROMOSSOMO - 1]):
            #     print("individuo ", novoIndividuo, "é pior q o melhor ",listaAuxiliar[0])

            #     print("Piorou com o score de", self.score)
            # else:
                # print("Melhorou com score de", self.score)
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)