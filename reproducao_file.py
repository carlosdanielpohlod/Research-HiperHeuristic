from mutacao_file import *
from utils import *
from random import *
from storage.database.crud import salvarHeuristicaUsada
class Reproduzir:
    def __init__(self, parametros, funcaoObjetivo, mutacao):
        self.parametros = parametros
        self.funcaoObjetivo = funcaoObjetivo
        self.score = 0
        self.mutacao = mutacao
        self.codMutacao = 0
    
    def mediaPais(self, pai01, pai02):
        return (pai01[self.parametros.TAMCROMOSSOMO - 1] + pai02[self.parametros.TAMCROMOSSOMO - 1]) / 2
        
    def mediaFilhos(self, listaAuxiliar, pai01, pai02):
        somatorio = 0
        
        for i in range(len(listaAuxiliar)):
            if((pai01 != listaAuxiliar[i]) and (pai02 != listaAuxiliar[i])):
                somatorio = listaAuxiliar[i][self.parametros.TAMCROMOSSOMO - 1] + somatorio
        return somatorio / (len(listaAuxiliar) - 2)

    def calcularScore(self, pai01, pai02, listaAuxiliar):
        mediapais = self.mediaPais(pai01,pai02)
        mediaFilhos = self.mediaFilhos(listaAuxiliar, pai01, pai02)
        diferenca = ((mediapais - mediaFilhos)) 
        self.score = (diferenca * mediapais) / 10000
        
    def reproduzir(self, populacao, fluxo, distancias, pai01, pai02, indiceReproducao):
        if(indiceReproducao == 1):
            self.reproduzir01(populacao, fluxo, distancias, pai01, pai02)
        if(indiceReproducao == 2):
            self.reproduzir02(populacao, fluxo, distancias, pai01, pai02)
        
    def aux_mutacao(self, novoIndividuo, fluxo, distancias):
        if(self.mutacao.chanceMutar()):
            
            individuoCopia = copy.deepcopy(novoIndividuo)
            self.mutacao.mutar(novoIndividuo, self.codMutacao, fluxo, distancias)
            self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
            self.mutacao.calcularScore(individuoCopia[self.parametros.TAMCROMOSSOMO - 1], novoIndividuo[self.parametros.TAMCROMOSSOMO - 1])

            if(individuoCopia[self.parametros.TAMCROMOSSOMO - 1] < novoIndividuo[self.parametros.TAMCROMOSSOMO - 1]):
                novoIndividuo = copy.deepcopy(individuoCopia)
            salvarHeuristicaUsada(self.parametros.idExecucao, self.parametros.MUTACAO, self.codMutacao, self.score)    
            
        else:
            self.mutacao.score = 0
    def log(self,pai01, pai02, filho):
        print(f'{filho[self.parametros.TAMCROMOSSOMO - 1]} filho de {pai01[self.parametros.TAMCROMOSSOMO - 1]} | {pai02[self.parametros.TAMCROMOSSOMO - 1]}')
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
            # self.log(populacao[pai01], populacao[pai02], novoIndividuo)
        
        
        utils.ordenar(listaAuxiliar)
        
        if(listaAuxiliar[0] != novoIndividuo): 
            self.calcularScore(populacao[pai01], populacao[pai02], listaAuxiliar)
        
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)

        # print(f'manteve {listaAuxiliar[0]} | {listaAuxiliar[1]}')



        
        salvarHeuristicaUsada(self.parametros.idExecucao, self.parametros.REPRODUCAO, 1, self.score)
    
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
            # self.log(populacao[pai01], populacao[pai02], novoIndividuo)
            utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
            
        utils.ordenar(listaAuxiliar)
       
        if(listaAuxiliar[0] != novoIndividuo):
            
            self.calcularScore(populacao[pai01], populacao[pai02], listaAuxiliar)
       
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)

        # print(f'manteve {listaAuxiliar[0][self.parametros.TAMCROMOSSOMO - 1]} | {listaAuxiliar[1][self.parametros.TAMCROMOSSOMO - 1]} score: {self.score}')
        salvarHeuristicaUsada(self.parametros.idExecucao, self.parametros.REPRODUCAO, 2, self.score)