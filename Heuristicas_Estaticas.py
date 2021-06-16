from parametros_file import *
from buscaLocal_file import BuscaLocal
from funcaoObjetivo_file import *
from selecaoPais_file import SelecaoPais
from reproducao_file import Reproduzir
from codHeuristicas import CodHeuristicas
from storage.database.crud import *
from heuristica import *
from escolha.HeuristicaEscolha import *
from utils import *
from mutacao_file import Mutacao
from numpy import mean, std

idExecucao = novaExecucao()

parametros = Parametros()
parametros.idExecucao = idExecucao
utils = Utils(parametros)
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
mutacao = Mutacao(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo, mutacao)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()

# ['1,3,1','1,2,3','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3']
heuristicas = ['1,1,1','1,1,2','1,1,3','1,2,1','1,2,2','1,2,3','1,3,1','1,3,2','1,3,3','2,1,1','2,1,2','2,1,3','2,2,1','2,2,2','2,2,3','2,3,1','2,3,2','2,3,3']

def heuristica_estatica(fluxo, distancias, tamInstancia, numExecucoes, instancia, multiplicador = 20):
    infoInstancia = ''
    parametros.setN(tamInstancia)
    for string in heuristicas:
        piorFinal = [] #
        melhorFinal = [] #
        somatorio = 0
        infoInstancia = f'{instancia} reproducao = {string[0]} busca local = {string[2]} mutacao = {string[4]}'
       
        for j in range(0, numExecucoes):

            idExecucao = novaExecucao()
            parametros.idExecucao = idExecucao

            melhorResultado = 999999999999999
            populacao = utils.declararMatriz(linhas = parametros.TAMPOPULACAO, colunas = parametros.TAMCROMOSSOMO)
            funcaoObjetivo.gerarPopulacao(populacao)
            funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)
            
            # print(populacao)
            codHeuristicas.codReproducao = string[0]
            codHeuristicas.codBuscaLocal = string[2]
            codHeuristicas.codMutacao = string[4]

            for i in range(tamInstancia * multiplicador): 
                melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
                # print('melhorResultado',melhorResultado)
            somatorio = somatorio + melhorResultado
            melhorFinal.append(melhorResultado) #
            # print('somatorio e melhorFinal', somatorio, melhorFinal)
            piorFinal.append(populacao[utils.buscarPiorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1]) 
        resultado_N_Execucoes(instancia = infoInstancia,idExecucaoInicial = idExecucao - numExecucoes, idExecucaoFinal = idExecucao, piorFinal = max(piorFinal, key=int), mediaMelhores = mean(melhorFinal), melhorIndividuo = min(melhorFinal), desvioPadrao = std(melhorFinal))


    
    
    
    
    







    


