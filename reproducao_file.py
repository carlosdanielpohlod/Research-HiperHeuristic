from mutacao_file import *
from utils import *
class Reproduzir:
    def __init__(self, parametros, funcaoObjetivo):
        self.parametros = parametros
        self.funcaoObjetivo = funcaoObjetivo
  
    def reproduzir(self, populacao, fluxo, distancias, pai01, pai02, indiceReproducao):
        if(indiceReproducao == 1):
            self.reproduzir01(populacao, fluxo, distancias, pai01, pai02)
        


    def reproduzir01(self, populacao, fluxo, distancias, pai01, pai02):
        
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
                genePassado = randint(0, self.parametros.N - 1)
                
                if(escolhido == 0):
                    # while(jaExiste(novoIndividuo, populacao[pai01][genePassado])):
                    while(populacao[pai01][genePassado] in novoIndividuo):
                        genePassado = randint(0, self.parametros.N - 1)
                    
                    novoIndividuo[i] = populacao[pai01][genePassado]
                    
                else:
                    # while(jaExiste(novoIndividuo, populacao[pai02][genePassado])):
                    while(populacao[pai02][genePassado] in novoIndividuo):
                    
                        genePassado = randint(0, self.parametros.N - 1)
                    
                    novoIndividuo[i] = populacao[pai02][genePassado]
                    
                
            
            if(mutacao.chanceMutar(self.parametros.PORCENTAGEMMUTACOES)):
                mutacao.mutar(novoIndividuo, 1)
            
            self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
            # *numAvaliacao = *numAvaliacao + 1
            
            utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
            
        
        
        utils.ordenar(listaAuxiliar)
        print(listaAuxiliar)
        # print(listaAuxiliar[2][12])
        input()
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)
    