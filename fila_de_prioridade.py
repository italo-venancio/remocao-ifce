from listaLigada import ListaLigada
from celula import Celula
from professor import Professor

class Fila_de_prioridade:
    def __init__(self):
        self.__elementos = ListaLigada()

    def push(self, professor): # insere de forma decrescente pela prioridade
        if self.empty() == True:
            self.__elementos.adicionar_comeco(professor)
        else:
            nova_celula = Celula()
            nova_celula.elemento = professor
            nova_celula.prioridade = professor.tempo_de_ifce   

            atual = self.__elementos._ListaLigada__primeira

            if atual.proxima == None and nova_celula.prioridade < atual.prioridade: # fila tem um elemento
                self.__elementos.adicionar_fim(professor)

            elif atual.proxima == None and nova_celula.prioridade > atual.prioridade: # fila tem um elemento
                self.__elementos.adicionar_comeco(professor)

            else: # fila tem dois ou mais elementos
                if nova_celula.prioridade > atual.prioridade:
                    self.__elementos.adicionar_comeco(professor)
                
                else:
                    insercao = False

                    while atual.proxima != None:
                        if nova_celula.prioridade > atual.proxima.prioridade:
                            nova_celula.proxima = atual.proxima
                            atual.proxima = nova_celula
                            insercao = True
                            break
                        atual = atual.proxima

                    if atual.prioridade > nova_celula.prioridade and insercao==False:
                        self.__elementos.adicionar_fim(professor)
            
    def pop(self):
        self.__elementos.remover_comeco()

    def empty(self):
        if self.__elementos.tamanho() == 0:
            return True
        return False

    def __str__(self):
        return self.__elementos.__str__()