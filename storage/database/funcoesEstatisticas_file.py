from estrutura_database import *
from utils_database import *
from grafico_file import Grafico

import numpy 
import peewee
db = peewee.SqliteDatabase('conhecimento.db')

class FuncoesEstatisticas:
    def getScoreHeuristica(self,heuristicaUsada_id, execucao_id):
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

    def getScoreHeuristicaSimplified(self,tipoHeuristica_id,codHeuristica,  execucao_id):
        
        
        result = HeuristicaUsada.select(HeuristicaUsada.heuristicaUsada_id).where(HeuristicaUsada.codHeuristica == codHeuristica, HeuristicaUsada.execucao_id == execucao_id, HeuristicaUsada.tipoHeuristica_id == codStringToNumber(tipoHeuristica_id)).execute()
        if(len(extrairHeuristicaUsada_id(result)) == 0):
            score = 'vazio'
            return score
        score = ScoreHeuristica.select(ScoreHeuristica.score).where(ScoreHeuristica.heuristicaUsada_id == extrairHeuristicaUsada_id(result)).execute()
        
        
        return extrairScoreHeuristica(score)

    def mediaHeuristicasExecucao(self,execucao_id):
        aux = extrairHeuristicaUsada_id(HeuristicaUsada.select(HeuristicaUsada.heuristicaUsada_id).where(HeuristicaUsada.execucao_id == execucao_id).execute())
        for i in range(len(aux)):
            mediaHeuristica(aux[i], execucao_id)

    def ultimaExecucao(self):
        ultimo = Execucao.select(Execucao.execucao_id).limit(1).order_by(Execucao.execucao_id.desc()).execute()
        for i in ultimo :
            return i.execucao_id
    
    def exibirEstatisticasIndividuais(self,tipo, heuristica):

        score = self.getScoreHeuristicaSimplified(heuristica,tipo,self.ultimaExecucao())
        
        count = 0
        somatorio = 0
        for i in score:
            if i == 0:
                count = count + 1
            else: 
                somatorio = i
        if(score == 'vazio'):
            score = 0
        else:
            print("Numero de chamadas ",len(score))
        
            print("media ",numpy.mean(int(somatorio)))
        print("\n", heuristica, tipo)
        print("zeros ", count)
        print("Execução id", self.ultimaExecucao())
        

    def exibirEstatisticasGerais(self,execucao_id,codReproducao,codMutacao,codBuscaLocal):
        result = Resultados.select().where(Resultados.codReproducao == codReproducao, Resultados.codMutacao == codMutacao, Resultados.codBuscaLocal == codBuscaLocal, Resultados.execucao_id == execucao_id).order_by(Resultados.fitness.desc()).execute()
        
        print(f'execucao da sequencia {codReproducao,codMutacao,codBuscaLocal}')
        for i in result:
            print(i.fitness)
            try:
                print(i.fitness)
            except:
                print('Nd')
    def mediaPopulacaoEFitnessPorExecucao(self,execucao_id):
        return extrairMediaPopulacaoEFitness(Resultados.select(Resultados.mediaPopulacao, Resultados.fitness).where(Resultados.execucao_id == execucao_id).execute())
    def codesPorExecucao(self,execucao_id):
        return extrairCodesResultados(Resultados.select(Resultados.codReproducao, Resultados.codBuscaLocal, Resultados.codMutacao).where(Resultados.execucao_id == execucao_id).execute())


# o = FuncoesEstatisticas()
# o.exibirEstatisticasIndividuais('reproducao',1)