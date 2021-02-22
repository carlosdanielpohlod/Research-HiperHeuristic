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




arquivo = ArquivosManager('storage/files/nug12.dat','r')
fluxo =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
distancias =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
arquivo.lerFluxo(fluxo)
arquivo.lerDistancias(distancias)

parametros = Parametros()

utils = Utils()
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
mutacao = Mutacao(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo, mutacao)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()

heuristicaEscolha = HeuristicaEscolha(ThompsonSampling())


# heuristicaEscolha.inicializar({'1,2,3','3,1,1','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3'})
heuristicas = ['1,3,1','1,2,3','3,1,1','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3']
populacao = utils.declararMatriz(linhas = parametros.TAMPOPULACAO, colunas = parametros.TAMCROMOSSOMO)



heuristicaEscolha  = HeuristicaEscolha(RandomChoice())    
heuristicaEscolha.inicializar([codHeuristicas.qtdReproducao,codHeuristicas.qtdBuscaLocal,codHeuristicas.qtdMutacao])
print('executando ...')
somatorio = 0
for i in range(10):

    funcaoObjetivo.gerarPopulacao(populacao)
    funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)
    idExecucao = novaExecucao()
    parametros.idExecucao = idExecucao
    print("Id da execucao ", idExecucao)

    for i in range(40):
        codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codMutacao = heuristicaEscolha.escolher()    
        melhorResultado = construirHeuristica(populacao,reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
    
        salvarResultado(idExecucao, codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codMutacao, melhorResultado )
    somatorio = somatorio + melhorResultado
    print('Melhor Individuo ', melhorResultado)
print("Media final -> ", somatorio/10)   
        
    
    
    
    
    







    


