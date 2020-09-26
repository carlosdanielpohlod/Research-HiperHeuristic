class ArquivosManager:
    def __init__(self, nome, operacao):
        self.file = open(nome, operacao)
    def lerFluxo(self, fluxo):
        # texto = []
        texto = self.file.readlines()
        for i in range(12):
            for j in range (12):
                fluxo[i][j] = texto[i].split(' ')

        print(fluxo)
fluxo =  [[0 for x in range(15)] for y in range(15)]
arquivo = ArquivosManager('storage/files/nug12.dat','r')
arquivo.lerFluxo(fluxo)