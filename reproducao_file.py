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
        novoIndividuo = [0] * len(populacao[0])
        genePassado = 0
        listaAuxiliar = [[0 for y in range(self.parametros.TAMCROMOSSOMO)]  for x in range(self.parametros.NUMMAXIMOFILHOS + 2)]
        contadorAuxiliar = 0
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai01])
        contadorAuxiliar = contadorAuxiliar + 1 
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai02])
        N = len(populacao[0])
        for filho in range(self.parametros.NUMMAXIMOFILHOS):
            contadorAuxiliar = contadorAuxiliar + 1
            genePassado = 0
            escolhido = 0
            utils.zerar(novoIndividuo)
            # novoIndividuo = [self.parametros.TAMCROMOSSOMO + 3]
            
        for i in range(N):
            escolhido = randint(0,2)
            genePassado = randint(0, N - 1)

            if(escolhido == 0):
                # while(jaExiste(novoIndividuo, populacao[pai01][genePassado])):
                while(populacao[pai01][genePassado] in novoIndividuo):
                    genePassado = randint(0, N - 1)
                
                novoIndividuo[i] = populacao[pai01][genePassado]
            else:
                # while(jaExiste(novoIndividuo, populacao[pai02][genePassado])):
                while(populacao[pai02][genePassado] in novoIndividuo):
                    genePassado = randint(0, N - 1)
                
                    novoIndividuo[i] = populacao[pai02][genePassado]
            
        
        if(mutacao.chanceMutar(self.parametros.PORCENTAGEMMUTACOES)):
            mutacao.mutar(novoIndividuo)

        self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
        # *numAvaliacao = *numAvaliacao + 1
        
        utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
        
    
    
        utils.ordenar(listaAuxiliar)
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)
    