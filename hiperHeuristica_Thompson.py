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
    
    populacao = utils.declararMatriz(linhas = parametros.TAMPOPULACAO, colunas = parametros.TAMCROMOSSOMO)

    
    somatorio = 0

    mi = []
    mf = []
    melhorResultado = parametros.INFINITO
    for i in range(numExecucoes): 
        
        heuristicaEscolha  = HeuristicaEscolha(ThompsonSampling())  
        
        heuristicaEscolha.inicializar(heuristicas)
        
        funcaoObjetivo.gerarPopulacao(populacao)
        
        funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)
        
        idExecucao = novaExecucao()
        parametros.idExecucao = idExecucao

        utils.bubbleSort(populacao)
        
        mi.append(populacao[0][parametros.TAMCROMOSSOMO - 1])


        salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
        
        for i in range(2*tamInstancia):
            utils.setCodigosHeuriticas(codHeuristicas, heuristicaEscolha.escolher())
            
            melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
            
            reward = int(reproducao.score + mutacao.score + buscaLocal.score)
            stringAlgoritmoUsado = utils.codToString(codHeuristicas)
            
            utils.sumRecompensas(reward, stringAlgoritmoUsado, heuristicaEscolha)
            
        somatorio = somatorio + melhorResultado
        mf.append(melhorResultado)
   
    print(mi)
    print('')
    print(mf)


        

        







    


