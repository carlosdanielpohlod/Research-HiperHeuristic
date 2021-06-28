from hiperHeuristica_Thompson import *
# from Heuristicas_Estaticas import heuristica_estatica
from hiperHeristica_Aleatoria import *
arquivo = ArquivosManager()
nomes =  [

    'storage/files/nug/nug16b.dat',
    
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
    # hiperHeuristica_Aleatoria(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 2, instancia = nome, multiplicador = 5)
    hiperHeuristica_Thompson(fluxo = fluxo, distancias = distancias, tamInstancia = arquivo.tam, numExecucoes = 30, instancia = nome, multiplicador = 20, arrayFixo = arrayFixo, variar = variar)
print("Execução finalizada !")
