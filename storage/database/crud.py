from storage.database.estrutura_database import Resultados,db
import peewee
db = peewee.SqliteDatabase('conhecimento.db')




def salvarResultado(codReproducao, codBuscaLocal, codSelecaoPais, fitness):
    
    try:
        db.connect()
        # data = [{"codReproducao=  codReproducao,"codBuscaLocal": 0, "codSelecaoPais": codSelecaoPais, "fitness": "100"}]
        resultados = Resultados(codReproducao =  codReproducao,codBuscaLocal=  0, codSelecaoPais=  codSelecaoPais, fitness= 100)
        resultados.save()
        
        print('inserido', resultados)
        resultados = Resultados()
        resultados = resultados.select(codReproducao).execute()

        
        for resultado in resultados:
            print(resultado.codReproducao)
        db.close()
    except NameError:
        print(NameError)
    class Meta:
        database = db

