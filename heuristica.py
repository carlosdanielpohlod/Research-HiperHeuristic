from utils import Utils
from random import *
from storage.files.operacaoArquivos import *

utils = Utils()
arquivo = ArquivosManager('storage/files/nug12.dat','r')
fluxo =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
distancias =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
arquivo.lerFluxo(fluxo)
arquivo.lerDistancias(distancias)

def construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas):
    utils = Utils(parametros)
    reproducao.codMutacao = codHeuristicas.codMutacao
    
    populacao = utils.declararMatriz(linhas = parametros.TAMPOPULACAO, colunas = parametros.TAMCROMOSSOMO)
    funcaoObjetivo.gerarPopulacao(populacao)
    funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)

    for i in range(15):    
        pai01, pai02 = selecaoPais.selecionar(populacao, fluxo, distancias)  
        reproducao.reproduzir(populacao, fluxo, distancias, pai01, pai02, codHeuristicas.codReproducao)
        
        utils.bubbleSort(populacao)
        melhor = randint(0,4) 
        buscaLocal.busca(populacao[melhor], fluxo, distancias, codHeuristicas.codBuscaLocal)    
        
    return populacao[melhor][parametros.TAMCROMOSSOMO - 1]