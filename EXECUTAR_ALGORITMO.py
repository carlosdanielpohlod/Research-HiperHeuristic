from hiperHeuristica_Thompson import *
# from Heuristicas_Estaticas import heuristica_estatica
from hiperHeristica_Aleatoria import *
arquivo = ArquivosManager()
nomes = [
    '/content/HiperHeuristic/storage/files/nug/nug12.dat',
    '/content/HiperHeuristic/storage/files/nug/nug14.dat',
    '/content/HiperHeuristic/storage/files/nug/nug15.dat',
    '/content/HiperHeuristic/storage/files/nug/nug16a.dat',
    '/content/HiperHeuristic/storage/files/nug/nug16b.dat',
    '/content/HiperHeuristic/storage/files/nug/nug17.dat',
    '/content/HiperHeuristic/storage/files/nug/nug18.dat',

'/content/HiperHeuristic/storage/files/nug/nug20.dat',

'/content/HiperHeuristic/storage/files/nug/nug21.dat',
'/content/HiperHeuristic/storage/files/nug/nug22.dat',
'/content/HiperHeuristic/storage/files/nug/nug25.dat',
'/content/HiperHeuristic/storage/files/nug/nug27.dat',


'/content/HiperHeuristic/storage/files/nug/nug28.dat'



]
for nome in nomes:

        
    print('Instancia Sendo executada: ', nome)
    arrayFixo = [1,1]
    variar = 'geral'

    arquivo.setParams(nome , 'r')

    fluxo =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
    distancias =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
    arquivo.lerFluxo(fluxo)
    arquivo.lerDistancias(distancias)

    # heuristica_estatica(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30, instancia = nome,multiplicador = 20)
    # hiperHeuristica_Aleatoria(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30, instancia = nome, multiplicador = 20)
    hiperHeuristica_Thompson(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30, instancia = nome, multiplicador = 20, arrayFixo = arrayFixo, variar = variar)
print("Execução finalizada !")
