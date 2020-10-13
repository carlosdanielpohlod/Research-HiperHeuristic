from parametros_file import *
from buscaLocal_file import BuscaLocal
from funcaoObjetivo_file import *
from selecaoPais_file import SelecaoPais
from reproducao_file import Reproduzir

global codigoTipoReproducao
codigoTipoReproducao = 0
global codigoTipoMutacao
codigoTipoMutacao = 0
global codigoTipoBuscaLocal
codigoTipoBuscaLocal = 0

fluxo = [   [0,1,2,3,1,2,3,4,2,3,4,5],
            [1,0,1,2,2,1,2,3,3,2,3,4],
            [2,1,0,1,3,2,1,2,4,3,2,3],
            [3,2,1,0,4,3,2,1,5,4,3,2],
            [1,2,3,4,0,1,2,3,1,2,3,4],
            [2,1,2,3,1,0,1,2,2,1,2,3],
            [3,2,1,2,2,1,0,1,3,2,1,2],
            [4,3,2,1,3,2,1,0,4,3,2,1],
            [2,3,4,5,1,2,3,4,0,1,2,3],
            [3,2,3,4,2,1,2,3,1,0,1,2],
            [4,3,2,3,3,2,1,2,2,1,0,1],
            [5,4,3,2,4,3,2,1,3,2,1,0]
        ]
distancias = [
            [0,5,2,4,1,0,0,6,2,1,1,1],
            [5,0,3,0,2,2,2,0,4,5,0,0],
            [2,3,0,0,0,0,0,5,5,2,2,2],
            [4,0,0,0,5,2,2,10,0,0,5,5],
            [1,2,0,5,0,10,0,0,0,5,1,1],
            [0,2,0,2,10,0,5,1,1,5,4,0],
            [0,2,0,2,0,5,0,10,5,2,3,3],
            [6,0,5,10,0,1,10,0,0,0,5,0],
            [2,4,5,0,0,1,5,0,0,0,10,10],
            [1,5,2,0,5,5,2,0,0,0,5,0],
            [1,0,2,5,1,4,3,5,10,5,0,2],
            [1,0,2,5,1,0,3,0,10,0,2,0]
        ]

def construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros):
    utils = Utils(parametros)
    numeroGeracoes = 0
    populacao = [[0 for x in range(parametros.TAMCROMOSSOMO)] for y in range(parametros.TAMPOPULACAO)]
    funcaoObjetivo.gerarPopulacao(populacao)
    funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)
    while(numeroGeracoes < 1):
        # print(numeroGeracoes)
        pai01, pai02 = selecaoPais.selecionar(populacao, 1)  
        reproducao.reproduzir(populacao, fluxo, distancias, pai01, pai02, 2)
        melhor = utils.buscarMelhorIndividuo(populacao)
        buscaLocal.busca(populacao[melhor], fluxo, distancias, 1)
        numeroGeracoes = numeroGeracoes + 1
    # print(populacao[melhor])
    
    





#int main(){
numExecucoes = 0
while(numExecucoes < 30):
    numExecucoes = numExecucoes + 1
    parametros = Parametros()
    selecaoPais = SelecaoPais(parametros)
    funcaoObjetivo = FuncaoObjetivo(parametros)
    reproducao = Reproduzir(parametros, funcaoObjetivo)
    buscaLocal = BuscaLocal(parametros, funcaoObjetivo)
    construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros)
    
#}

