import random
class RandomChoice:
    def __init__(self):
        self.qtdReproducao = 0
        self.qtdBuscaLocal = 0
        self.qtdMutacao = 0
    def inicializar(self, info):
        self.qtdReproducao = int(info[0])
        self.qtdBuscaLocal = int(info[1])
        self.qtdMutacao = int(info[2])
    def atualizar(self, info):
        print("No action")
        return
    def escolher(self, excluir = None):
        if(excluir == None):
            return [random.randint(1, self.qtdReproducao),random.randint(1, self.qtdBuscaLocal), random.randint(1, self.qtdMutacao)]
        else:
            combinacao = [random.randint(1, self.qtdReproducao),random.randint(1, self.qtdBuscaLocal), random.randint(1, self.qtdMutacao)]
            print(combinacao, excluir)
            while(combinacao in excluir):
                print("refeito a combinacao")
                print(combinacao, excluir)
                combinacao = [random.randint(1, self.qtdReproducao),random.randint(1, self.qtdBuscaLocal), random.randint(1, self.qtdMutacao)]
            return combinacao

    