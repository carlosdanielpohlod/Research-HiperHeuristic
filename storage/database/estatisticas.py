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

def getScoreHeuristicaSimplified(tipoHeuristica_id,codHeuristica,  execucao_id):
    

    result = HeuristicaUsada.select(HeuristicaUsada.heuristicaUsada_id).where(HeuristicaUsada.codHeuristica == codHeuristica, HeuristicaUsada.execucao_id == execucao_id, HeuristicaUsada.tipoHeuristica_id == codStringToNumber(tipoHeuristica_id)).execute()
    score = ScoreHeuristica.select(ScoreHeuristica.score).where(ScoreHeuristica.heuristicaUsada_id == extrairHeuristicaUsada_id(result)).execute()
    print(extrairScoreHeuristica(score))


def mediaHeuristicasExecucao(execucao_id):
    aux = extrairHeuristicaUsada_id(HeuristicaUsada.select(HeuristicaUsada.heuristicaUsada_id).where(HeuristicaUsada.execucao_id == execucao_id).execute())
    for i in range(len(aux)):
        mediaHeuristica(aux[i], execucao_id)

def ultimaExecucao():
    ultimo = Execucao.select(Execucao.execucao_id).limit(1).order_by(Execucao.execucao_id.desc()).execute()
    for i in ultimo :
        return i.execucao_id



getScoreHeuristicaSimplified('reproducao',1,ultimaExecucao())


    




