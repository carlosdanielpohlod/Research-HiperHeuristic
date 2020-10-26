from storage.database.estrutura_database import Resultados,db
import peewee
db = peewee.SqliteDatabase('conhecimento.db')




def salvarResultado(codReproducao, codBuscaLocal, codSelecaoPais, fitness):
    
    # try:
    # db.connect()
    resultados = Resultados(codReproducao =  codReproducao,codBuscaLocal=  codBuscaLocal, codSelecaoPais=  codSelecaoPais, fitness= fitness)
    resultados.save()
    db.close()
    print("Melhor resultado salvo")
    # except peewee.OperationalError:
    #     print("erro", peewee.OperationalError)
    class Meta:
        database = db

def melhorHeuristica():
    
    try:
        db.connect()
        resultados = Resultados()
        resultados = resultados.select().order_by("fitness").limit(1).execute()
        
        for resultado in resultados:
            return [resultado.codReproducao, resultado.codBuscaLocal, resultado.codSelecaoPais, resultado.fitness]
        
        db.close()
    except peewee.OperationalError:
        print("erro", peewee.OperationalError)
    class Meta:
        database = db