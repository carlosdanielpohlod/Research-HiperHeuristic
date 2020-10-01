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
        N = len(fluxo[0]) 
        utils = Utils(self.parametros)
        mutacao = Mutacao()
        escolhido = 0
        novoIndividuo = [0] * (N)
        genePassado = 0
        listaAuxiliar = [[0 for y in range(self.parametros.TAMCROMOSSOMO)]  for x in range(self.parametros.NUMMAXIMOFILHOS + 2)]
        contadorAuxiliar = 0
        
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai01])
        
        contadorAuxiliar = contadorAuxiliar + 1 
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai02])
        print("antes do for")
        for filho in range(self.parametros.NUMMAXIMOFILHOS):
            contadorAuxiliar = contadorAuxiliar + 1
            genePassado = 0
            escolhido = 0
            print("bug")
            utils.zerar(novoIndividuo)
            # novoIndividuo = [self.parametros.TAMCROMOSSOMO + 3]
        
        for i in range(N):
            escolhido = randint(0,1)
            genePassado = randint(0, N - 2)
            
            if(escolhido == 0):
                # while(jaExiste(novoIndividuo, populacao[pai01][genePassado])):
                while(populacao[pai01][genePassado] in novoIndividuo):
                    genePassado = randint(0, N - 2)
                
                novoIndividuo[i] = populacao[pai01][genePassado]
                print(novoIndividuo)
            else:
                # while(jaExiste(novoIndividuo, populacao[pai02][genePassado])):
                while(populacao[pai02][genePassado] in novoIndividuo):
                    print(populacao[pai02][genePassado])
                    print(novoIndividuo)
                    genePassado = randint(0, N - 2)
                
                novoIndividuo[i] = populacao[pai02][genePassado]
                print(novoIndividuo)
            
        
        if(mutacao.chanceMutar(self.parametros.PORCENTAGEMMUTACOES)):
            mutacao.mutar(novoIndividuo, 1)

        self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
        # *numAvaliacao = *numAvaliacao + 1
        print('aa')
        utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
        
    
    
        utils.ordenar(listaAuxiliar)
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)
    