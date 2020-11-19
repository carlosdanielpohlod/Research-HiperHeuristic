from parametros_file import *
from buscaLocal_file import BuscaLocal
from funcaoObjetivo_file import *
from selecaoPais_file import SelecaoPais
from reproducao_file import Reproduzir
from codHeuristicas import CodHeuristicas
# from storage.database.crud import *
from heuristica import *

parametros = Parametros()
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = FuncaoObjetivo(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo)
buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
codHeuristicas = CodHeuristicas()

codHeuristicas.codReproducao, codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais, codHeuristicas.fitness = [1,1,1,1000]
#Hiper Heuritica
somatorio = 0
scoreAuxilio = 0
heuristicaAuxilio = 0



for i in range(50):
    codHeuristicas.codBuscaLocal = randint(1,3) # 2 = 1.0
    melhorResultado = construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros, codHeuristicas)
    # print(reproducao.score)
    if(buscaLocal.score > scoreAuxilio):
        scoreAuxilio = buscaLocal.score
        heuristicaAuxilio = codHeuristicas.codBuscaLocal
    else:
        codHeuristicas.codBuscaLocal = heuristicaAuxilio 
   
    if(melhorResultado > codHeuristicas.fitness):
        
        codHeuristicas.codReproducao = randint(1,2) # 1 = 0.4
        
        codHeuristicas.codSelecaoPais = randint(1,2) # 3 = 3.9
    else:
        codHeuristicas.fitness = melhorResultado

# if(input("Quer salvar o resultado?")  == 's'):
#     salvarResultado(codHeuristicas.codReproducao, codHeuristicas.codBuscaLocal, codHeuristicas.codSelecaoPais, "Media: ", somatorio/10)

    


