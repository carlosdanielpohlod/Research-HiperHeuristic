from utils import Utils
from random import *
from storage.database.crud import salvarResultado

utils = Utils()


def construirHeuristica(populacao, reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas):
    utils = Utils(parametros)
    reproducao.codMutacao = codHeuristicas.codMutacao
    
   

    for i in range(15):    
        pai01, pai02 = selecaoPais.melhorEAleatorio(populacao)  
        reproducao.reproduzir(populacao, fluxo, distancias, pai01, pai02, codHeuristicas.codReproducao)
        
        utils.bubbleSort(populacao)
        melhor =  utils.buscarMelhorIndividuo(populacao)

        buscaLocal.busca(populacao[melhor], fluxo, distancias, codHeuristicas.codBuscaLocal)    
        # salvarResultado(codExecucao=parametros.idExecucao, codBuscaLocal=codHeuristicas.codBuscaLocal,codReproducao=codHeuristicas.codBuscaLocal,codMutacao=codHeuristicas.codMutacao, fitness=float(populacao[melhor][parametros.TAMCROMOSSOMO - 1]))
    return populacao[melhor][parametros.TAMCROMOSSOMO - 1]