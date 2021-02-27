from utils import Utils
from random import *
from storage.database.crud import salvarResultado

utils = Utils()


def construirHeuristica(populacao, reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas):
    utils = Utils(parametros)
    reproducao.codMutacao = codHeuristicas.codMutacao
    
   

    for i in range(2):    
        pai01, pai02 = selecaoPais.melhorEAleatorio(populacao)  
        reproducao.reproduzir(populacao, fluxo, distancias, pai01, pai02, codHeuristicas.codReproducao)
        
        utils.bubbleSort(populacao)
        escolhido = randint(0, 3)
        buscaLocal.busca(populacao[escolhido], fluxo, distancias, codHeuristicas.codBuscaLocal)  
        melhor = utils.buscarMelhorIndividuo(populacao)  
        salvarResultado(mediaPopulacao = utils.mediaPopulacao(populacao), codExecucao=parametros.idExecucao, codHeuristicas = codHeuristicas, fitness=float(populacao[melhor][parametros.TAMCROMOSSOMO - 1]))
    return populacao[melhor][parametros.TAMCROMOSSOMO - 1]