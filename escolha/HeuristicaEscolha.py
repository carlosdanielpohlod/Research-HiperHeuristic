
class HeuristicaEscolha:
    
    def __init__(self, method):
        self.dependencia = method
    def escolher(self, info = None):
        if(info != None):
            return self.dependencia.escolher(info)
        else:
            return self.dependencia.escolher()
    def inicializar(self, info):
        return self.dependencia.inicializar(info)
    def atualizar(self, info):
        return self.dependencia.atualizar(info)