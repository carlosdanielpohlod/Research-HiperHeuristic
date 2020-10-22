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



#Hiper Heuritica
codHeuristicas.codReproducao, codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais, codHeuristicas.fitness = melhorHeuristica()

for i in range(10):

    melhorResultado = construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
    if(melhorResultado < codHeuristicas.fitness):
        codHeuristicas.fitness = melhorResultado
    else:
        codHeuristicas.codBuscaLocal = 1
        codHeuristicas.codReproducao = 1
        codHeuristicas.codSelecaoPais = randint(1, 2)
salvarResultado(codHeuristicas.codReproducao, codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais, codHeuristicas.fitness)

    


