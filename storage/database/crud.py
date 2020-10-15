from storage.database.estrutura_database import Resultados,db

def salvarResultado(codReproducao, codBuscaLocal, codSelecaoPais, fitness):

    resultados = Resultados.insert(codReproducao = codReproducao,codBuscaLocal = 0, 
    codSelecaoPais = codSelecaoPais,
    fitness = fitness
    ).execute()
    print('inserido', resultados)
    class Meta:
        database = db

