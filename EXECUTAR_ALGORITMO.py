from hiperHeuristica_Thompson import *
from Heuristicas_Estaticas import heuristica_estatica
# from hiperHeristica_Aleatoria import *
arquivo = ArquivosManager()
nomes = arquivo.allFilesDir(prefix=True)
# del(nomes[0:8])
for nome in nomes:

        
    print('Instancia Sendo executada: ', nome)
    arquivo.setParams(nome , 'r')

    fluxo =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
    distancias =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
    arquivo.lerFluxo(fluxo)
    arquivo.lerDistancias(distancias)
    heuristica_estatica(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30, instancia = nome,multiplicador = 20)
    # hiperHeuristica_Aleatoria(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30, instancia = nome)
    # hiperHeuristica_Thompson(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30, instancia = nome)
print("Execução finalizada !")
