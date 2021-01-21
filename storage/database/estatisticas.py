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


def mediaHeuristica(heuristicaUsada_id, execucao_id):
    result = getScoreHeuristica(heuristicaUsada_id, execucao_id)
    med = mediaScore(result[0])
    print(f'média {result[1]} {result[2]}: {med:.2f}')
def mediaHeuristicasExecucao(execucao_id):
    aux = extrairHeuristicaUsada_id(HeuristicaUsada.select(HeuristicaUsada.heuristicaUsada_id).where(HeuristicaUsada.execucao_id == execucao_id).execute())
    for i in range(len(aux)):
        mediaHeuristica(aux[i], execucao_id)



mediaHeuristicasExecucao(3)
    




