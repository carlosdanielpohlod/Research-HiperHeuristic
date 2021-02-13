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

idExecucao = novaExecucao()

parametros = Parametros()
parametros.idExecucao = idExecucao
utils = Utils()
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
mutacao = Mutacao(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo, mutacao)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()
jaInseridos = []

heuristicaEscolha = HeuristicaEscolha(ThompsonSampling())


heuristicaEscolha.inicializar({'1,2,3','3,1,1','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3'})

for i in range(80):
    utils.setCodigosHeuriticas(codHeuristicas, heuristicaEscolha.escolher())
    melhorResultado = construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
    utils.sumRecompensas(reproducao.score,f'{codHeuristicas.codReproducao},{codHeuristicas.codBuscaLocal},{codHeuristicas.codMutacao}', heuristicaEscolha)

    # salvarResultado(idExecucao, codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codMutacao, melhorResultado )
     




# heuristicaEscolha  = HeuristicaEscolha(RandomChoice())    
# heuristicaEscolha.inicializar([codHeursticas.qtdReproducao,codHeuristicas.qtdBuscaLocal,codHeuristicas.qtdMutacao])

# for i in range(20):
#     codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codMutacao = heuristicaEscolha.escolher()    
#     melhorResultado = construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
    
#     salvarResultado(idExecucao, codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codMutacao, melhorResultado )
    
    
    
    
    
    
    







    


