from parametros_file import *
from buscaLocal_file import BuscaLocal
from funcaoObjetivo_file import *
from selecaoPais_file import SelecaoPais
from reproducao_file import Reproduzir
from codHeuristicas import CodHeuristicas
from storage.database.crud import *
from heuristica import *
from escolha.ThompsonSampling import *
from escolha.HeuristicaEscolha import *
from utils import *
from mutacao_file import Mutacao
from escolha.RandomChoice import RandomChoice
from random import *
from storage.files.operacaoArquivos import *


def hiperHeuristica_Aleatoria(fluxo, distancias, tamInstancia, numExecucoes):
    
    

    parametros = Parametros()
    utils = Utils(parametros)
    selecaoPais = SelecaoPais(parametros)
    funcaoObjetivo = FuncaoObjetivo(parametros)
    mutacao = Mutacao(parametros)
    reproducao = Reproduzir(parametros, funcaoObjetivo, mutacao)
    buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
    codHeuristicas = CodHeuristicas()
    
    parametros.setN(tamInstancia)
    
    heuristicaEscolha = HeuristicaEscolha(RandomChoice())
    heuristicaEscolha.inicializar([codHeuristicas.qtdReproducao,codHeuristicas.qtdBuscaLocal,codHeuristicas.qtdMutacao])

    populacao = utils.declararMatriz(linhas = parametros.TAMPOPULACAO, colunas = parametros.TAMCROMOSSOMO)

    
    somatorio = 0

    piorFinal = [] #
    melhorFinal = [] #
    melhorResultado = parametros.INFINITO
    for i in range(numExecucoes): 

        funcaoObjetivo.gerarPopulacao(populacao)
        funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)
        idExecucao = novaExecucao()
        parametros.idExecucao = idExecucao
        print(' ')
        print("Id da execucao ", idExecucao)
        utils.bubbleSort(populacao)
        for i in range(tamInstancia * 2):
            codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codMutacao = heuristicaEscolha.escolher()    
            melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
        
            salvarResultado(idExecucao, codHeuristicas, melhorResultado, utils.mediaPopulacao(populacao) )
        somatorio = somatorio + melhorResultado
        melhorFinal.append(melhorResultado)
        piorFinal.append(populacao[utils.buscarPiorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1])
    print('Piores finais', piorFinal)
    print('melhores finais', melhorFinal)
    print('media melhores',mean(melhorFinal))
    print('melhor final', min(melhorFinal))
    print('desvo padrao', std(melhorFinal))
    print('Pior final',max(piorFinal, key=int))
  
            
        
        
        
        
        







    


