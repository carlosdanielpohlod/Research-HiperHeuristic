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

parametros = Parametros()
    
utils = Utils(parametros)
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
mutacao = Mutacao(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo, mutacao)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()
# multiplicador = 20

def reproducaoVariada(fluxo, distancias, tamInstancia, numExecucoes, instancia, multiplicador, arrayFixo):
 
    heuristicas = ['1','2']
    somatorio = 0
    parametros.setN(tamInstancia)

    codHeuristicas.buscaLocal, codHeuristicas.codMutacao = arrayFixo
    instancia = f'{instancia} b = {arrayFixo[0]} m = {arrayFixo[1]}'
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
        
        utils.bubbleSort(populacao)
        

        salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
        
        for i in range(tamInstancia * multiplicador):

            stringAlgoritmoUsado = heuristicaEscolha.escolher()
            codHeuristicas.codReproducao = int(stringAlgoritmoUsado)
            
            melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
            # print(melhorResultado)
            reward = int(reproducao.score)
            utils.sumRecompensas(reward, stringAlgoritmoUsado, heuristicaEscolha)
            salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
            for individuo in populacao:
                funcaoObjetivo.infactivelCheck(fluxo, distancias,individuo, instancia)
        somatorio = somatorio + melhorResultado

        melhorFinal.append(melhorResultado) #
        piorFinal.append(populacao[utils.buscarPiorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1]) #
   
    resultado_N_Execucoes(instancia = instancia,idExecucaoInicial = idExecucao - numExecucoes, idExecucaoFinal = idExecucao, piorFinal = max(piorFinal, key=int), mediaMelhores = mean(melhorFinal), melhorIndividuo = min(melhorFinal), desvioPadrao = int(std(melhorFinal)))


def mutacaoVariada(fluxo, distancias, tamInstancia, numExecucoes, instancia, multiplicador, arrayFixo):
    heuristicas = ['1','2','3']
    somatorio = 0
    parametros.setN(tamInstancia)

    codHeuristicas.reproducao, codHeuristicas.buscaLocal = arrayFixo
    instancia = f'{instancia} r = {arrayFixo[0]} b = {arrayFixo[1]}'
#1,1
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
        
        utils.bubbleSort(populacao)
        

        salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
        
        for i in range(tamInstancia * multiplicador):

            stringAlgoritmoUsado = heuristicaEscolha.escolher()
            codHeuristicas.mutacao = int(stringAlgoritmoUsado)
            
            melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
            
            reward = int(mutacao.score)
            utils.sumRecompensas(reward, stringAlgoritmoUsado, heuristicaEscolha)
            salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
            for individuo in populacao:
                funcaoObjetivo.infactivelCheck(fluxo, distancias,individuo, instancia)
        somatorio = somatorio + melhorResultado

        melhorFinal.append(melhorResultado) #
        piorFinal.append(populacao[utils.buscarPiorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1]) #
   
    resultado_N_Execucoes(instancia = instancia,idExecucaoInicial = idExecucao - numExecucoes, idExecucaoFinal = idExecucao, piorFinal = max(piorFinal, key=int), mediaMelhores = mean(melhorFinal), melhorIndividuo = min(melhorFinal), desvioPadrao = int(std(melhorFinal)))
 




def buscaLocalVariada(fluxo, distancias, tamInstancia, numExecucoes, instancia, multiplicador, arrayFixo):
    heuristicas = ['1','2','3']
    somatorio = 0
    parametros.setN(tamInstancia)

    codHeuristicas.reproducao, codHeuristicas.codMutacao = arrayFixo
    instancia = f'{instancia} r = {arrayFixo[0]} m = {arrayFixo[1]}'
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
        
        utils.bubbleSort(populacao)
        

        salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
        
        for j in range(tamInstancia * multiplicador):

            stringAlgoritmoUsado = heuristicaEscolha.escolher()
            codHeuristicas.buscaLocal = int(stringAlgoritmoUsado)
            
            melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
            
            reward = int(buscaLocal.score)
            utils.sumRecompensas(reward, stringAlgoritmoUsado, heuristicaEscolha)
            
            for individuo in populacao:
                funcaoObjetivo.infactivelCheck(fluxo, distancias,individuo, instancia)
        somatorio = somatorio + melhorResultado

        melhorFinal.append(melhorResultado) #
        piorFinal.append(populacao[utils.buscarPiorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1]) #
        salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
    resultado_N_Execucoes(instancia = instancia,idExecucaoInicial = idExecucao - numExecucoes, idExecucaoFinal = idExecucao, piorFinal = max(piorFinal, key=int), mediaMelhores = mean(melhorFinal), melhorIndividuo = min(melhorFinal), desvioPadrao = int(std(melhorFinal)))
      



def geral(fluxo, distancias, tamInstancia, numExecucoes, instancia, multiplicador = 20):
    
    
    
    heuristicas = ['1,3,1','1,2,3','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3']
    parametros.setN(tamInstancia)
    somatorio = 0
    # instancia = f'{instancia} thompson geral'
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
        # print('id', idExecucao)
        utils.bubbleSort(populacao)
        

        salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
        
        for j in range(tamInstancia * multiplicador):
            
            utils.setCodigosHeuriticas(codHeuristicas, heuristicaEscolha.escolher())
            
            melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
            
            reward = int(reproducao.score + mutacao.score + buscaLocal.score)
            stringAlgoritmoUsado = utils.codToString(codHeuristicas)
            
            utils.sumRecompensas(reward, stringAlgoritmoUsado, heuristicaEscolha)
            salvarResultado(codExecucao = idExecucao, codHeuristicas = codHeuristicas, fitness = populacao[utils.buscarMelhorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1], mediaPopulacao = utils.mediaPopulacao(populacao) )
            for individuo in populacao:
                funcaoObjetivo.infactivelCheck(fluxo, distancias,individuo, instancia)
        somatorio = somatorio + melhorResultado

        melhorFinal.append(melhorResultado) #
        piorFinal.append(populacao[utils.buscarPiorIndividuo(populacao)][parametros.TAMCROMOSSOMO - 1]) #

    resultado_N_Execucoes(instancia = instancia,idExecucaoInicial = idExecucao - numExecucoes, idExecucaoFinal = idExecucao, piorFinal = max(piorFinal, key=int), mediaMelhores = mean(melhorFinal), melhorIndividuo = min(melhorFinal), desvioPadrao = std(melhorFinal))

def hiperHeuristica_Thompson(fluxo, distancias, tamInstancia, numExecucoes, instancia, multiplicador, arrayFixo, variar):
    if(variar == 'reproducao'):
        return reproducaoVariada(fluxo, distancias, tamInstancia, numExecucoes, instancia,multiplicador, arrayFixo)
    if(variar == 'busca local'):
        return buscaLocal(fluxo, distancias, tamInstancia, numExecucoes, instancia,multiplicador, arrayFixo)
    if(variar == 'mutacao'):
        return mutacaoVariada(fluxo, distancias, tamInstancia, numExecucoes, instancia,multiplicador, arrayFixo)
    if(variar == 'geral'):
        return geral(fluxo, distancias, tamInstancia, numExecucoes, instancia,multiplicador)


        

        






    


