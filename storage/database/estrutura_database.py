import peewee

db = peewee.SqliteDatabase('conhecimento.db')
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
# criarTabelas()


