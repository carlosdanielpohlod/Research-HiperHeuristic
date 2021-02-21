from estrutura_database import *
from utils_database import *


import numpy 
import peewee
db = peewee.SqliteDatabase('conhecimento.db')


def getScoreHeuristica(heuristicaUsada_id, execucao_id):
    nome = None
    aux = None
    result = ScoreHeuristica.select(ScoreHeuristica.score).join(
        HeuristicaUsada,on=(ScoreHeuristica.heuristicaUsada_id == HeuristicaUsada.heuristicaUsada_id)
    ).where(HeuristicaUsada.execucao_id == execucao_id, ScoreHeuristica.heuristicaUsada_id == heuristicaUsada_id).execute()
    
    heuristica = TipoHeuristica.select(TipoHeuristica.nome).join(HeuristicaUsada, on=(HeuristicaUsada.tipoHeuristica_id == TipoHeuristica.tipoHeuristica_id)).where(HeuristicaUsada.heuristicaUsada_id == heuristicaUsada_id).execute()
    code = HeuristicaUsada.select(HeuristicaUsada.codHeuristica).where(HeuristicaUsada.heuristicaUsada_id == heuristicaUsada_id).execute()

    return [result, getNome(heuristica), getCodeHeuristica(code)]


# def mediaHeuristica(heuristicaUsada_id, execucao_id):
#     result = getScoreHeuristica(heuristicaUsada_id, execucao_id)
#     med = mediaScore(result[0])
#     print(f'média {result[1]} {result[2]}: {med:.2f}')

def getScoreHeuristicaSimplified(tipoHeuristica_id,codHeuristica,  execucao_id):
    
    
    result = HeuristicaUsada.select(HeuristicaUsada.heuristicaUsada_id).where(HeuristicaUsada.codHeuristica == codHeuristica, HeuristicaUsada.execucao_id == execucao_id, HeuristicaUsada.tipoHeuristica_id == codStringToNumber(tipoHeuristica_id)).execute()
    print(extrairHeuristicaUsada_id(result))
    score = ScoreHeuristica.select(ScoreHeuristica.score).where(ScoreHeuristica.heuristicaUsada_id == extrairHeuristicaUsada_id(result)).execute()
    if score == None:
        score = 0
    
    return extrairScoreHeuristica(score)

def mediaHeuristicasExecucao(execucao_id):
    aux = extrairHeuristicaUsada_id(HeuristicaUsada.select(HeuristicaUsada.heuristicaUsada_id).where(HeuristicaUsada.execucao_id == execucao_id).execute())
    for i in range(len(aux)):
        mediaHeuristica(aux[i], execucao_id)

def ultimaExecucao():
    ultimo = Execucao.select(Execucao.execucao_id).limit(1).order_by(Execucao.execucao_id.desc()).execute()
    for i in ultimo :
        return i.execucao_id

def exibirResultados(k, heuristica):

    score = getScoreHeuristicaSimplified(heuristica,k,ultimaExecucao())
    count = 0
    somatorio = 0
    for i in score:
        if i == 0:
            count = count + 1
        else: 
            somatorio = i
    print("\n", heuristica, k)
    print("zeros ", count)
    print("Execução id", ultimaExecucao())
    print("Numero de chamadas ",len(score))
    print("media ",numpy.mean(somatorio))

def exibirEstatisticasGerais(execucao_id,codReproducao,codMutacao,codBuscaLocal):
    result = Resultados.select().where(Resultados.codReproducao == codReproducao, Resultados.codMutacao == codMutacao, Resultados.codBuscaLocal == codBuscaLocal, Resultados.execucao_id == execucao_id).order_by(Resultados.fitness.desc()).execute()
    # print(result)
    print(f'execucao da sequencia {codReproducao,codMutacao,codBuscaLocal}')
    for i in result:
        try:
            print(i.fitness)
        except:
            print('Nd')
        
heuristicas = ['1,2,3','3,1,1','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3']

# for i in heuristicas:
   
#     exibirEstatisticasIndividuais(int(i[0]),'reproducao')
#     exibirEstatisticasIndividuais(int(i[2]),'busca local')
#     exibirEstatisticasIndividuais(int(i[4]),'mutacao')

# for i  in range(1,3):
#     exibirEstatisticasIndividuais(i, 'reproducao')

# for i in range(1,4):
#    exibirEstatisticasIndividuais(i, 'busca local')
# for i in range(1,4):
#     exibirEstatisticasIndividuais(i, 'mutacao')



