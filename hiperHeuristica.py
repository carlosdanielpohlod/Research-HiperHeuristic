from parametros_file import *
from buscaLocal_file import BuscaLocal
from funcaoObjetivo_file import *
from selecaoPais_file import SelecaoPais
from reproducao_file import Reproduzir
from codHeuristicas import CodHeuristicas
from storage.database.crud import *
from heuristica import *

parametros = Parametros()
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()
somatorio = 0
scoreAuxilio = 0
heuristicaAuxilio = 0



idExecucao = novaExecucao()

codHeuristicas.codReproducao, codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais, codHeuristicas.fitness = [1,1,1,1000]

for i in range(50):
    
    melhorResultado = construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
    
  



    


