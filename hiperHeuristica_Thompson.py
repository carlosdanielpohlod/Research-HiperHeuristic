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
from numpy import mean, std

def hiperHeuristica_Thompson(fluxo, distancias, tamInstancia, numExecucoes):

    parametros = Parametros()
    utils = Utils(parametros)
    selecaoPais = SelecaoPais(parametros)
    funcaoObjetivo = FuncaoObjetivo(parametros)
    mutacao = Mutacao(parametros)
    reproducao = Reproduzir(parametros, funcaoObjetivo, mutacao)
    buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
    codHeuristicas = CodHeuristicas()
    heuristicas = ['0,0,0','1,3,1','1,2,3','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3']
    parametros.setN(tamInstancia)
    somatorio = 0

    piorFinal = [] #
    melhorFinal = [] #
    
    for i in range(numExecucoes): 
        populacao = utils.declararMatriz(linhas = parametros.TAMPOPULACAO, colunas = parametros.TAMCROMOSSOMO)

    
        

        melhorResultado = parametros.INFINITO
        heuristicaEscolha  = HeuristicaEscolha(ThompsonSampling())  
        
        heuristicaEscolha.inicializar(heuristicas)
        
        funcaoObjetivo.gerarPopulacao(populacao)
        
        funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)
        
        idExecucao = novaExecucao()
        parametros.idExecucao = idExecucao
        print('id', idExecucao)
        utils.bubbleSort(populacao)
        

        salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
        
        for i in range(2*tamInstancia):
            utils.setCodigosHeuriticas(codHeuristicas, heuristicaEscolha.escolher())
            
            melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
            
            reward = int(reproducao.score + mutacao.score + buscaLocal.score)
            stringAlgoritmoUsado = utils.codToString(codHeuristicas)
            
            utils.sumRecompensas(reward, stringAlgoritmoUsado, heuristicaEscolha)
            
        somatorio = somatorio + melhorResultado

        melhorFinal.append(melhorResultado) #
        piorFinal.append(populacao[utils.buscarPiorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1]) #
   

    print('Piores finais', piorFinal)
    print('melhores finais', melhorFinal)
    print('media melhores',mean(melhorFinal))
    print('melhor final', min(melhorFinal))
    print('desvo padrao', std(melhorFinal))
    print('Pior final',max(piorFinal, key=int))
    


        

        







    


