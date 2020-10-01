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
    numeroGeracoes = 0
    N = len(fluxo[0])
    pai01 = 0
    pai02 = 0
    populacao = [[0 for x in range(parametros.TAMCROMOSSOMO)] for y in range(parametros.TAMPOPULACAO)]
    aux = []
    funcaoObjetivo.gerarPopulacao(populacao)
    # selecaoPais.selecionar(populacao, 1)
    
    funcaoObjetivo.avaliarPopulacao(populacao, fluxo, distancias)

    # reproducao.reproduzir(populacao, fluxo, distancias, pai01, pai02, 1)
    # while (numeroGeracoes < 10):
    #     funcaoObjetivo.gerarPopulacao(populacao)
    #     aux = selecaoPais.selecionarPais(1)
    #     pai01 = aux[0]
    #     pai02 = aux[1]
    #     reproducao.reproduzir(populacao, fluxo, distancias, pai01, pai02, 1)
    #     buscaLocal.busca(fluxo, distancias, 1)

#int main(){

parametros = Parametros()
parametros.setParametros(3,4,6)
selecaoPais = SelecaoPais(parametros)
funcaoObjetivo = funcaoObjetivo(parametros)
reproducao = Reproduzir(parametros, funcaoObjetivo)
# buscalLocal = BuscalLocal(parametros)
buscaLocal = []
construirHeuristica(reproducao, buscaLocal, funcaoObjetivo, selecaoPais, fluxo, distancias, parametros)
#}

