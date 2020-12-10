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

parametros = Parametros()
utils = Utils()
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
mutacao = Mutacao(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo, mutacao)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()
jaInseridos = []




# idExecucao = novaExecucao()




heuristicaEscolha  = HeuristicaEscolha(RandomChoice())    
heuristicaEscolha.inicializar([2,3,3])

for i in range(50):
    codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal,codHeuristicas.codMutacao = heuristicaEscolha.escolher()
    melhorResultado = construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
    print(melhorResultado)
    # stringAlgoritmoUsado = utils.codToString(codHeuristicas)
    # salvarResultado(idExecucao, codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais, melhorResultado )
    # if(stringAlgoritmoUsado not in jaInseridos):
    #     heuristicaEscolha.inicializar([stringAlgoritmoUsado])
    #     jaInseridos.append(stringAlgoritmoUsado)

    # utils.sumRecompensas((reproducao.score + buscaLocal.score), stringAlgoritmoUsado, heuristicaEscolha)
    # if(i < 20):
    #     utils.setCodigosHeuriticas(codHeuristicas=codHeuristicas, codigos='random')
        
    # else: 
    #     escolhido = heuristicaEscolha.escolher()
        
    #     utils.setCodigosHeuriticas(codHeuristicas, escolhido)
    # print("CodMutação ", reproducao.codMutacao)
    
    
    







    


