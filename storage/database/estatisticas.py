from estrutura_database import * 
import peewee
db = peewee.SqliteDatabase('conhecimento.db')

def mediaHeuristica(heuristicaUsada_id, execucao_id):
    result = ScoreHeuristica.select(ScoreHeuristica.score).join(
        HeuristicaUsada,on=(ScoreHeuristica.heuristicaUsada_id == HeuristicaUsada.heuristicaUsada_id)
    ).where(HeuristicaUsada.execucao_id == execucao_id, ScoreHeuristica.heuristicaUsada_id == heuristicaUsada_id).execute()
    for i in result:
        print(i.score)
mediaHeuristica(3,2)
    
# SELECT scoreheuristica.score FROM scoreheuristica JOIN heuristicausada 
# ON heuristicausada.codHeuristica = scoreheuristica.heuristicaUsada_id
# WHERE heuristicausada.execucao_id = 2 AND heuristicausada.codHeuristica = 1