class ArquivosManager:
    def __init__(self, nome, operacao):
        self.file = open(nome, operacao)
        self.dadosArquivo = self.file.readlines()
        self.tam = self.tamanhoInstancia()
    def tamanhoInstancia(self):
        
        tamanho = self.dadosArquivo[0].split(' ')
        tamanho = tamanho[0].replace('\n','')
        return int(tamanho)
    def lerFluxo(self, fluxo):
        k = 2
        i = 0
        while(k < self.tam + 2):
            fluxo[i] = self.dadosArquivo[k].split(' ')
            for j in range(self.tam):
                fluxo[i][j] = fluxo[i][j].replace('\n','')
            k = k + 1
            i = i + 1
        self.castToInt(fluxo)
    def retirarCampoVazio(self, vetor):
        # linhas = len(vetor[0])
        while '' in vetor:
            vetor.remove('')

    def lerDistancias(self, distancias):
        k = self.tam + 3
        i = 0
        while(k < self.tam + self.tam + 3):
            distancias[i] = self.dadosArquivo[k].split(' ')
            self.retirarCampoVazio(distancias[i])
            for j in range(self.tam):
                # print("aqui", distancias[i])
                distancias[i][j] = distancias[i][j].replace('\n','')
            k = k + 1
            i = i + 1
        self.castToInt(distancias)
    def castToInt(self, matriz):
        linhas = len(matriz)
        colunas = len(matriz[0])
        for i in range(linhas):
            for j in range(colunas):
                matriz[i][j] = int(matriz[i][j])



