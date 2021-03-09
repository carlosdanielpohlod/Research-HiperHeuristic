
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
class Grafico:

    def evolucaoPopulacaoXBest(self,evolucaoPopulacao, evolucaoBest, id):
        x = np.arange(1, len(evolucaoPopulacao) + 1)
        plt.plot(x, evolucaoPopulacao, x, evolucaoBest)
        
        plt.grid(True)

        plt.show()
        # plt.savefig(f'{id}' )

    def particionarVetor(self, vetor, partes):
        particionado = []
        i = 0
        while i < len(vetor) - partes:
            parte = []
            for j in range(partes):
                parte.append(vetor[i])
                i = i+1
            particionado.append(parte)
        
        return particionado  
    
    def graficoArea(self, rows):
        y = self.particionarVetor(rows, 5)
        labels = ['0,0,0','1,3,1','1,2,3','3,1,1','1,3,2','2,3,1','2,1,2','1,2,1','2,2,1','1,1,1','2,2,2','2,3,3','2,1,3','2,1,1','1,2,2','1,3,3']
        x = []
        for i in range(6):
            x.append(i)
        y = self.matriz_stringToId(y, labels)
    
        labels = []
        fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
        ax.stackplot(x, y, labels=labels)
       
        # ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.02))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ',')))
        plt.margins(0, 0.1)
        plt.show()


    def graficoSimples(self,y):
        x = np.arange(1, len(y) + 1)
        plt.plot(x, y)

        plt.grid(True)

        plt.show()