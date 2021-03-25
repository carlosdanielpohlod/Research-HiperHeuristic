# from hiperHeuristica_Thompson import *
from hiperHeristica_Aleatoria import *
arquivo = ArquivosManager()
nomes = arquivo.allFilesDir(prefix=True)
del(nomes[0:8])
for nome in nomes:
    # try:
        
        print('Instancia ', nome)
        arquivo.setParams(nome , 'r')

        fluxo =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
        distancias =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
        arquivo.lerFluxo(fluxo)
        arquivo.lerDistancias(distancias)
        hiperHeuristica_Aleatoria(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30)
        # hiperHeuristica_Thompson(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30)
        
    # except(Exception):
    #     print("erro em: ",nome)
    #     continue
