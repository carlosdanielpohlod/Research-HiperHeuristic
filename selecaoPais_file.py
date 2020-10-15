from random import randint
class SelecaoPais:
    def __init__(self, parametros):
        self.parametros = parametros
    def selecionar(self, populacao, codigoSelecao):
        aux = []
        if(codigoSelecao == 1):
           return self.escolherPais01(populacao)
        if(codigoSelecao == 2):
            return self.selecaoAleatoria(populacao)
    def selecaoAleatoria(self, populacao):
        pai01 = 0
        pai02 = 0
        while(pai01 == pai02):
            pai01 = randint(0, self.parametros.TAMPOPULACAO - 1)
            pai02 = randint(0, self.parametros.TAMPOPULACAO - 1)
        return pai01, pai02
    def somatorioFitnessPopulacao(self, populacao):
    
        somatorio = 0
        for  i in range(self.parametros.TAMPOPULACAO):
            somatorio = somatorio + populacao[i][self.parametros.TAMCROMOSSOMO - 1]
        return somatorio
    def selecaoComum(self, populacao, pai01,  pai02, mediaPopulacao):
    
        for i in range(self.parametros.TAMPOPULACAO):
            if(populacao[i][self.parametros.TAMCROMOSSOMO - 1] >= mediaPopulacao):
                pai01 = i
                break
            
        
        for i in range(self.parametros.TAMPOPULACAO):
            if(populacao[i][self.parametros.TAMCROMOSSOMO - 1] < mediaPopulacao):
                pai02 = i
                break
        return [pai01, pai02]
            
    
    

    def escolherPais01(self, populacao):
        mediaHabilidade = 0.0
        mediaPais = 0 
        minimoAceitavel = 0 
        mediaPopulacao = 0.0 
        somatorioPopulacao = 0 
        encontrado = False
        antiCrash = 0
        pai01 = 0
        pai02 = 0
        pai01 = randint(0, self.parametros.TAMPOPULACAO - 1)
        pai02 = randint(0, self.parametros.TAMPOPULACAO - 1)
        while(pai01 == pai02):
           
            pai01 = randint(0, self.parametros.TAMPOPULACAO - 1)
            pai02 = randint(0, self.parametros.TAMPOPULACAO - 1)
        
              
        somatorioPopulacao = self.somatorioFitnessPopulacao(populacao)
        
        mediaPopulacao = float(somatorioPopulacao / self.parametros.TAMPOPULACAO)
        
        
        while not encontrado:
           
            if antiCrash == self.parametros.TAMPOPULACAO * 3 :
                aux = []
                aux = self.selecaoComum(populacao, pai01, pai02, mediaPopulacao)
                return aux

            antiCrash = antiCrash + 1
            
            if(populacao[pai01][self.parametros.TAMCROMOSSOMO - 1] <= mediaPopulacao):
                
                while((populacao[pai02][self.parametros.TAMCROMOSSOMO - 1] <= mediaPopulacao)  or (pai01 == pai02)):
                    pai02 = randint(0, self.parametros.TAMPOPULACAO - 1)
                   
                
                encontrado = True
            else:
                if(populacao[pai02][self.parametros.TAMCROMOSSOMO - 1] <= mediaPopulacao):
                    while( (populacao[pai01][self.parametros.TAMCROMOSSOMO - 1] <= mediaPopulacao) or (pai01 == pai02)):
                        pai02 = randint(0, self.parametros.TAMPOPULACAO - 1)
                    
                    encontrado =True
        
        return [pai01, pai02]
            
        
        
        
       