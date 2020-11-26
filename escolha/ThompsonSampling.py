from thompson_sampling.bernoulli import BernoulliExperiment
from thompson_sampling.priors import BetaPrior

class ThompsonSampling:
    def __init__(self):
        self.beta = BetaPrior()
        self.experimento = BernoulliExperiment(priors=self.beta)
        
        
    def atualizarRecompensas(self,estrategias):
        for opcao in estrategias:
            self.experimento.addRewards([{estrategias['codHeuristicas']:['recompensa']}])
    def inicializar(self, estrategias):
        for opcao in estrategias:
            self.beta.add_one(mean=0.5, variance=0.2, effective_size=10, label=opcao['codHeuristica'])

    def escolher(self, estrategias):
        self.atualizarRecompensas(self.experimento, estrategias)

        return experimento.choose_arm()
        
        
