import os
from storage.config import storage_path
class ArquivosManager:
    def __init__(self):
        self.file = None
        self.dadosArquivo = None
        self.tam = None

    def setParams(self, nome, operacao):
        self.file = open(nome, operacao)
        self.dadosArquivo = self.file.readlines()
        self.tam = self.tamanhoInstancia()
    
    def allFilesDir(self, pasta = f'{storage_path}/files/nug', prefix = False):
        caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
        if not prefix:
            caminhos = [i.removeprefix(f'{pasta}\\') for i in caminhos]
        return caminhos

    def tamanhoInstancia(self):
        
        tamanho = self.dadosArquivo[0].split(' ')
        tamanho = tamanho[0].replace('\n','')
        return int(tamanho)
    def lerDistancias(self, distancias):
        k = 2
        i = 0
        while(k < self.tam + 2):
            
            distancias[i] = self.dadosArquivo[k].split(' ')
            
            for j in range(self.tam):
                distancias[i][j] = distancias[i][j].replace('\n','')
            k = k + 1
            i = i + 1
        self.castToInt(distancias)
    def retirarCampoVazio(self, vetor):
        # linhas = len(vetor[0])
        while '' in vetor:
            vetor.remove('')

    def lerFluxo(self, fluxo):
        k = self.tam + 3
        i = 0
        
        while(k < self.tam + self.tam + 3):
            # try:
                
                fluxo[i] = self.dadosArquivo[k].split(' ')
                self.retirarCampoVazio(fluxo[i])
                for j in range(self.tam):
                    # print("aqui", fluxo[i])
                    fluxo[i][j] = fluxo[i][j].replace('\n','')
                k = k + 1
                i = i + 1
            # except Exception as ist:
            #     print(ist.args)
                
            #     print('k: ', k)
            #     print('dados arquivo de k: ', self.dadosArquivo[33:59])
            #     # print('fluxo ', fluxo)
            #     input("pressione uma tecla")
        self.castToInt(fluxo)
      
    def castToInt(self, matriz):
        linhas = len(matriz)
        colunas = len(matriz[0])
        for i in range(linhas):
            for j in range(colunas):
                matriz[i][j] = int(matriz[i][j])



