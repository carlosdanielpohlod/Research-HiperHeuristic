from storage.database.estrutura_database import Resultados,db,ScoreHeuristica,Execucao,HeuristicaUsada,Resultado_N_Execucoes
import peewee
db = peewee.SqliteDatabase('conhecimento.db')




def salvarResultado(codExecucao, codHeuristicas, fitness, mediaPopulacao):

    resultados = Resultados(execucao_id = codExecucao,mediaPopulacao = mediaPopulacao, codReproducao =  codHeuristicas.codReproducao,codBuscaLocal=  codHeuristicas.codBuscaLocal, codMutacao=  codHeuristicas.codMutacao, fitness= fitness)
    
    resultados.save()
    # print(codExecucao, codReproducao, codBuscaLocal, codMutacao, fitness)
    # print(resultados.fitness)
    db.close()
    # print("Salvo")
   
def salvarHeuristicaUsada(idExecucao, tipoHeuristica, codHeuristica, score ):
 
    result = HeuristicaUsada.get_or_create(tipoHeuristica_id = tipoHeuristica, execucao_id = idExecucao, codHeuristica = codHeuristica)
    salvarScore(result[0].heuristicaUsada_id, codHeuristica, score)     
    return 
def resultado_N_Execucoes(instancia, idExecucaoInicial, idExecucaoFinal, piorFinal, mediaMelhores, melhorIndividuo, desvioPadrao, ):
    r = Resultado_N_Execucoes(instancia = instancia, idExecucaoInicial = idExecucaoInicial, idExecucaoFinal = idExecucaoFinal, piorFinal = piorFinal, mediaMelhores = mediaMelhores, melhorIndividuo = melhorIndividuo, desvioPadrao = desvioPadrao )
    r.save()
    db.close()
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
