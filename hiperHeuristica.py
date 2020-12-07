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


parametros = Parametros()
utils = Utils()
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()
jaInseridos = []




# idExecucao = novaExecucao()

codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal,codHeuristicas.codSelecaoPais = [0,0,1]


heuristicaEscolha  = HeuristicaEscolha(ThompsonSampling())    
for i in range(400):
    
    melhorResultado = construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
    stringAlgoritmoUsado = utils.codToString(codHeuristicas)

    if(stringAlgoritmoUsado not in jaInseridos):
        heuristicaEscolha.inicializar([stringAlgoritmoUsado])
        jaInseridos.append(stringAlgoritmoUsado)


    reward = reproducao.score + buscaLocal.score #score() retorna 1 se score > 0; senao retorna 0
    utils.sumRecompensas(reward, stringAlgoritmoUsado, heuristicaEscolha)
    if(i < 20):
        utils.setCodigosHeuriticas(codHeuristicas=codHeuristicas, codigos='random')
        
    else: 
        escolhido = heuristicaEscolha.escolher()
        
        utils.setCodigosHeuriticas(codHeuristicas, escolhido)
    # salvarResultado(idExecucao, codHeuristicas.codReproducao,codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais, melhorResultado )
        
    
    







    


