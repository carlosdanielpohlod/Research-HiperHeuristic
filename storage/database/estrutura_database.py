import peewee

db = peewee.SqliteDatabase('conhecimento.db')

class Resultados(peewee.Model):
    fitness = peewee.DoubleField()
    codReproducao = peewee.IntegerField()
    codBuscaLocal = peewee.IntegerField()
    codSelecaoPais = peewee.IntegerField()
    class Meta:
        database = db
def criarTabelas():
    try:
        resultados = Resultados()
        resultados.create_table()
        print("Tabela reultados foi criada")
    except NameError:
        print("erro", NameError)



