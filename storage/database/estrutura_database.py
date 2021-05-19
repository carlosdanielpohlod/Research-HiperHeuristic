import peewee
from storage.config import storage_path
db = peewee.SqliteDatabase(f'{storage_path}/conhecimento.db')
class Execucao(peewee.Model):
    execucao_id = peewee.IntegerField(primary_key=True)
    class Meta:
        database = db
        db_table = 'execucao'
class Resultados(peewee.Model):
    fitness = peewee.DoubleField()
    codReproducao = peewee.IntegerField()
    codBuscaLocal = peewee.IntegerField()
    codMutacao = peewee.IntegerField()
    mediaPopulacao = peewee.DoubleField(null = True)
    execucao = peewee.ForeignKeyField(Execucao,to_field= 'execucao_id')
    class Meta:
        database = db

class TipoHeuristica(peewee.Model):
    tipoHeuristica_id = peewee.IntegerField(primary_key=True)
    nome = peewee._StringField()

    class Meta:
        database = db
        
        db_table = 'tipoheuristica'
class Resultado_N_Execucoes(peewee.Model):
    id = peewee.IntegerField(primary_key=True)
  
    idExecucaoInicial = peewee.IntegerField(null = True)
    idExecucaoFinal = peewee.IntegerField(null = True)
    piorFinal = peewee.DoubleField(null = True) 
    mediaMelhores = peewee.DoubleField(null = True)
    melhorIndividuo = peewee.DoubleField(null = True)
    desvioPadrao = peewee.DoubleField(null = True)
    instancia = peewee._StringField(null = True)
    comentarios = peewee._StringField(null = True)
    class Meta:
        database = db
        db_table = 'resultado_N_execucoes'
class HeuristicaUsada(peewee.Model):
    heuristicaUsada_id = peewee.IntegerField(primary_key=True)
    tipoHeuristica = peewee.ForeignKeyField(TipoHeuristica,to_field= 'tipoHeuristica_id')
    execucao = peewee.ForeignKeyField(Execucao,to_field= 'execucao_id')
    codHeuristica = peewee.IntegerField()
    
    class Meta:
        database = db
        heuristica = peewee.CompositeKey('tipoHeuristica', 'execucao','codHeuristica')
        db_table = 'heuristicausada'
class ScoreHeuristica(peewee.Model):
    heuristicaUsada = peewee.ForeignKeyField(HeuristicaUsada,to_field= 'heuristicaUsada_id')
    score = peewee.DoubleField()
    class Meta:
        database = db
def criarTabelas():
    try:
        resultado_n_execucoes = Resultado_N_Execucoes()
        resultado_n_execucoes.create_table()
        print("Resultado_N_Execucoes criada")
    except NameError:
        print("erro", NameError)
    try:
        execucao = Execucao()
        execucao.create_table()
        print("Tabela execucao foi criada")
    except NameError:
        print("erro", NameError)
    try:
        resultados = Resultados()
        resultados.create_table()
        print("Tabela reultados foi criada")
    except NameError:
        print("erro", NameError)
    try:
        tipoHeuristica = TipoHeuristica()
        tipoHeuristica.create_table()
        print("Tabela tipo heuristica foi criada")
    except NameError:
        print("erro", NameError)
    try:
        heuristica = HeuristicaUsada()
        heuristica.create_table()
        print("Tabela heuristica foi criada")
    except NameError:
        print("erro", NameError)
    try:
        scoreHeuristica = ScoreHeuristica()
        scoreHeuristica.create_table()
        print("Tabela scoreHeuristica foi criada")
    except NameError:
        print("erro", NameError)
    
    db.execute_sql("INSERT INTO tipoheuristica (nome) VALUES('reprodução')")
    db.execute_sql("INSERT INTO tipoheuristica (nome) VALUES('busca local')")
    db.execute_sql("INSERT INTO tipoheuristica (nome) VALUES('mutação')")
    print("Tipos de heuristicas inseridos")
# criarTipos()
criarTabelas()


# tipoHeuristica = Resultado_N_Execucoes()
# tipoHeuristica.create_table()
