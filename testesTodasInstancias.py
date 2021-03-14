from hiperHeuristica_Thompson import *
arquivo = ArquivosManager()
nomes = arquivo.allFilesDir(prefix=True)

for nome in nomes:
    try:
        arquivo.setParams(nome , 'r')

        fluxo =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
        distancias =  utils.declararMatriz(linhas=arquivo.tam, colunas=arquivo.tam)
        arquivo.lerFluxo(fluxo)
        arquivo.lerDistancias(distancias)
        
        hiperHeuristica_Thompson(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 2)
    except(Exception):
        print("erro em: ",nome)
        continue
