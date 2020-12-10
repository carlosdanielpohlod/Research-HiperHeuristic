from storage.database.estrutura_database import Resultados,db,ScoreHeuristica,Execucao,HeuristicaUsada
import peewee
db = peewee.SqliteDatabase('conhecimento.db')




def salvarResultado(codExecucao, codReproducao, codBuscaLocal, codMutacao, fitness):

    resultados = Resultados(execucao_id = codExecucao, codReproducao =  codReproducao,codBuscaLocal=  codBuscaLocal, codMutacao=  codMutacao, fitness= fitness)
    resultados.save()
    db.close()
    # print("Salvo")
   
def salvarHeuristicaUsada(idExecucao, tipoHeuristica, codHeuristica, score ):
    h = HeuristicaUsada
    result = h.select(h.heuristicaUsada_id).where((h.execucao_id == idExecucao)&
    (h.tipoHeuristica_id == tipoHeuristica)&(h.codHeuristica == codHeuristica)).limit(1)

    # print(result)
#   ARRUMAR AQUI
    for v in result: 
        result =  v.heuristicaUsada_id   
        print("Id ",v.heuristicaUsada_id)
        if(v == None):
            print("Numtem")
            new = HeuristicaUsada(tipoHeuristica_id = tipoHeuristica, execucao_id = idExecucao, codHeuristica = codHeuristica)
            result = new.save()
            print(result)
    # result = h.select('heuristicaUsada_id').where(h.execucao_id == idExecucao).where(h.tipoHeuristica_id == tipoHeuristica).where(h.codHeuristica == codHeuristica).limit(1).execute()
    # result = result.heuristicaUsada_id


    salvarScore(result, codHeuristica, score)     
    return 
def salvarScore(heuristicaUsada_id, codHeuristica, score):
    novoScore = ScoreHeuristica(heuristicaUsada_id = heuristicaUsada_id, codHeuristica = codHeuristica, score = score)
    novoScore.save()
    db.close()
    return
def novaExecucao():
    idExecucao = Execucao.insert().execute()
    
    db.close()
    
    return idExecucao
def melhorHeuristica():
    
    try:
        db.connect()
        resultados = Resultados()
        resultados = resultados.select().order_by("fitness").limit(1).execute()
        
        for resultado in resultados:
            return [resultado.codReproducao, resultado.codBuscaLocal, resultado.codMutacao, resultado.fitness]
        
        db.close()
    except peewee.OperationalError:
        print("erro", peewee.OperationalError)
    class Meta:
        database = db
