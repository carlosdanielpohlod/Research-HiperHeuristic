from funcoesEstatisticas_file import *
from grafico_file import *

grafico = Grafico()
funcoes = FuncoesEstatisticas()
def bestXmediaPop():
    best, pop = funcoes.mediaPopulacaoEFitnessPorExecucao(266)
    grafico.evolucaoPopulacaoXBest(best, pop)
def areaHeuristicas():
    grafico.graficoArea(funcoes.codesPorExecucao(266))
    
areaHeuristicas()