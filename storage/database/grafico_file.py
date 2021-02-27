
import numpy as np
import matplotlib.pyplot as plt

class Grafico:

    def evolucaoPopulacaoXBest(evolucaoPopulacao, evolucaoBest):
        x = np.arange(1, len(evolucaoPopulacao) + 1)
        plt.plot(x, evolucaoPopulacao, x, evolucaoBest)

        plt.grid(True)

        plt.show()
