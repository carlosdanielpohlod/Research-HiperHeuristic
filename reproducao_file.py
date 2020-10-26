from mutacao_file import *
from utils import *
from random import *
class Reproduzir:
    def __init__(self, parametros, funcaoObjetivo):
        self.parametros = parametros
        self.funcaoObjetivo = funcaoObjetivo
  
    def reproduzir(self, populacao, fluxo, distancias, pai01, pai02, indiceReproducao):
        if(indiceReproducao == 1):
            self.reproduzir01(populacao, fluxo, distancias, pai01, pai02)
        if(indiceReproducao == 2):
            self.reproduzir02(populacao, fluxo, distancias, pai01, pai02)
        


    def reproduzir01(self, populacao, fluxo, distancias, pai01, pai02):
        
        utils = Utils(self.parametros)
        mutacao = Mutacao()
        escolhido = 0
        novoIndividuo = [0] * (self.parametros.TAMCROMOSSOMO)
        genePassado = 0
        listaAuxiliar = [[0 for y in range(self.parametros.TAMCROMOSSOMO)]  for x in range(self.parametros.NUMMAXIMOFILHOS + 2)]
        contadorAuxiliar = 0
        
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai01])
        
        contadorAuxiliar = contadorAuxiliar + 1 
        utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai02])
        
        for filho in range(self.parametros.NUMMAXIMOFILHOS):
            contadorAuxiliar = contadorAuxiliar + 1
            genePassado = 0
            escolhido = 0
            novoIndividuo = [0] * self.parametros.TAMCROMOSSOMO 
            utils.zerar(novoIndividuo)
            
        
            for i in range(self.parametros.N):
                escolhido = randint(0,1)
                genePassado = randint(0, self.parametros.TAMCROMOSSOMO - 2)
                
                if(escolhido == 0):
                    # while(jaExiste(novoIndividuo, populacao[pai01][genePassado])):
                    while(populacao[pai01][genePassado] in novoIndividuo):
                        genePassado = randint(0, self.parametros.TAMCROMOSSOMO - 2)
                        
                    novoIndividuo[i] = populacao[pai01][genePassado]
                    
                else:
                    # while(jaExiste(novoIndividuo, populacao[pai02][genePassado])):
                    while(populacao[pai02][genePassado] in novoIndividuo):
                        
                        genePassado = randint(0, self.parametros.TAMCROMOSSOMO - 2)
                        
                    novoIndividuo[i] = populacao[pai02][genePassado]
                    
                
            
            if(mutacao.chanceMutar(self.parametros.PORCENTAGEMMUTACOES)):
                mutacao.mutar(novoIndividuo, 1)
            
            self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)

            # *numAvaliacao = *numAvaliacao + 1
            # contadorAuxiliar = contadorAuxiliar + 1
            utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
           
        
        
        utils.ordenar(listaAuxiliar)
        
        utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)

    
    def reproduzir02(self, populacao, fluxo, distancias, pai01, pai02):
        utils = Utils(self.parametros)
        numeroFilhos = randint(1, self.parametros.NUMMAXIMOFILHOS)
        maisPrivilegiado = 0
        listaAuxiliar = [[0 for y in range(self.parametros.TAMCROMOSSOMO)]  for x in range(self.parametros.NUMMAXIMOFILHOS + 2)]
        contadorAuxiliar = 0
        if(populacao[pai01][self.parametros.TAMCROMOSSOMO - 1] < populacao[pai02][self.parametros.TAMCROMOSSOMO - 1]):
            maisPrivilegiado = pai01
            menosPrivilegiado = pai02
        else:
            maisPrivilegiado = pai02
            menosPrivilegiado = pai01 
        novoIndividuo = [22] * self.parametros.TAMCROMOSSOMO
        for i in range(self.parametros.TAMCROMOSSOMO):
            i = randint(0, self.parametros.TAMCROMOSSOMO - 4)
            if(i + 2 >= self.parametros.TAMCROMOSSOMO - 1):
                i = 0
                novoIndividuo[i] = populacao[maisPrivilegiado][i]
            else:
                novoIndividuo[i] = populacao[maisPrivilegiado][i]
                i = i + 2
       
        
        
        for i in range(self.parametros.TAMCROMOSSOMO):
            indice = populacao[menosPrivilegiado][i]
            
            if((indice not in novoIndividuo)and utils.posicaoVazia(novoIndividuo) != None):
                novoIndividuo[utils.posicaoVazia(novoIndividuo)] = populacao[menosPrivilegiado][i]


        self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)


            
    # def reproduzir02(self, populacao, fluxo, distancias, pai01, pai02):

    #     utils = Utils(self.parametros)
    #     numeroFilhos = randint(1, self.parametros.NUMMAXIMOFILHOS)
    #     maisPrivilegiado = 0
    #     listaAuxiliar = [[0 for y in range(self.parametros.TAMCROMOSSOMO)]  for x in range(self.parametros.NUMMAXIMOFILHOS + 2)]
    #     contadorAuxiliar = 0
    #     cont = 0
        
    #     if(populacao[pai01][self.parametros.TAMCROMOSSOMO - 1] < populacao[pai02][self.parametros.TAMCROMOSSOMO - 1]):
    #         maisPrivilegiado = pai01
    #         menosPrivilegiado = pai02
    #     else:
    #         maisPrivilegiado = pai02
    #         menosPrivilegiado = pai01 

        
    #     utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai01])
        
    #     contadorAuxiliar = contadorAuxiliar + 1 
    #     utils.inserir(listaAuxiliar[contadorAuxiliar], populacao[pai02])

    #     for filho in range(numeroFilhos):
    #         novoIndividuo = [22] * self.parametros.TAMCROMOSSOMO
    #         contadorAuxiliar = contadorAuxiliar + 1
    #         utils.zerar(novoIndividuo)
            
    #         i = randint(0, self.parametros.TAMCROMOSSOMO - 4)
            
            
    #         while(cont < int(self.parametros.TAMCROMOSSOMO / 2 )):
                
    #             cont = cont + 1
    #             if(i + 2 >= self.parametros.TAMCROMOSSOMO - 1):
    #                 i = 0
    #                 novoIndividuo[i] = populacao[maisPrivilegiado][i]
    #             else:
    #                 novoIndividuo[i] = populacao[maisPrivilegiado][i]
    #                 i = i + 2
                        
    #         genePassado = 0  
    #         for i in range(int(self.parametros.TAMCROMOSSOMO / 3)):
               
    #             if(utils.existe(populacao[menosPrivilegiado][genePassado],novoIndividuo)):
                    
    #                 genePassado = randint(0, self.parametros.TAMCROMOSSOMO - 2)
    #             novoIndividuo[genePassado] = populacao[menosPrivilegiado][genePassado]
            
    #         while(utils.posicaoVazia(novoIndividuo) != None):
    #             # geneAleatorio = randint(0,self.parametros.TAMCROMOSSOMO - 2)
                
    #             pai = randint(0,1)
                
    #             if(pai == 0):
    #                 for i in range(self.parametros.TAMCROMOSSOMO - 1):
    
    
    
                        
    
    #                     if((populacao[pai01][i] not in novoIndividuo) and (utils.posicaoVazia(novoIndividuo) != None)):
                            
    #                         novoIndividuo[utils.posicaoVazia(novoIndividuo)] = populacao[pai01][i]
                            
    #             else:
    #                 for i in range(self.parametros.TAMCROMOSSOMO - 1):
    
    
    
                        
    
    #                     if((populacao[pai02][i] not in novoIndividuo)and (utils.posicaoVazia(novoIndividuo) != None)):
    #                         novoIndividuo[utils.posicaoVazia(novoIndividuo)] = populacao[pai02][i]          
                
    #         self.funcaoObjetivo.avaliarIndividuo(novoIndividuo, fluxo, distancias)
    #         # contadorAuxiliar = contadorAuxiliar + 1
    #         utils.inserir(listaAuxiliar[contadorAuxiliar], novoIndividuo)
          
    
    #     utils.ordenar(listaAuxiliar)
    
        
    #     utils.persistirMelhores(listaAuxiliar, populacao, pai01, pai02)
        



        