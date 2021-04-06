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


idExecucao = novaExecucao()

arquivo = ArquivosManager('storage/files/nug20.dat','r')
fluxo =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
distancias =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
arquivo.lerFluxo(fluxo)
arquivo.lerDistancias(distancias)

parametros = Parametros()
parametros.idExecucao = idExecucao
utils = Utils(parametros)
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
mutacao = Mutacao(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo, mutacao)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()

heuristicas = ['0,0,0','1,3,1','1,2,3','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3']
populacao = utils.declararMatriz(linhas = parametros.TAMPOPULACAO, colunas = parametros.TAMCROMOSSOMO)

for string in heuristicas:
    melhorResultado = 0
    somatorio = 0
    funcaoObjetivo.gerarPopulacao(populacao)
    funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)
    idExecucao = novaExecucao()
    parametros.idExecucao = idExecucao
    utils.bubbleSort(populacao)
    print('idExecucao ', idExecucao)
    print('melhor resultado antes ', populacao[0][parametros.TAMCROMOSSOMO - 1])
    codHeuristicas.codReproducao = string[0]
    codHeuristicas.codBuscaLocal = string[2]
    codHeuristicas.codMutacao = string[4]
    for i in range(10):
        
        
        melhorResultado = construirHeuristica(populacao, reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
        # salvarResultado(idExecucao, codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codMutacao, melhorResultado )
    print("Melhor resultado depois ",melhorResultado)
    somatorio = somatorio + melhorResultado 
print('media de ',string[0], string[2], string[4],' -> ', somatorio/10)


    
    
    
    
    







    


