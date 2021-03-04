
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
class Grafico:

    def evolucaoPopulacaoXBest(self,evolucaoPopulacao, evolucaoBest):
        x = np.arange(1, len(evolucaoPopulacao) + 1)
        plt.plot(x, evolucaoPopulacao, x, evolucaoBest)

        plt.grid(True)

        plt.show()



    def graficoArea(self, rows):
       
        names = []
        y = []
        labels = []
        # intervalo = int(len(rows) / 6)
        for i in range(len(rows) - 3):
            line = [3] 
            for j in range(i,i+3):
                line.append(rows[i])
            y.append(line)
            labels.append(i)
        x = np.arange(1, 4)
        
        fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
        ax.stackplot(x, y, labels=labels)

        # ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.02))
        # ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ',')))
        plt.margins(0, 0.1)
        plt.show()


    def graficoSimples(self,y):
        x = np.arange(1, len(y) + 1)
        plt.plot(x, y)

        plt.grid(True)

        plt.show()