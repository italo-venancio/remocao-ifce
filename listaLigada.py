from celula import Celula
from professor import Professor
 
class ListaLigada:
    def __init__(self):
        self.__primeira = None
        self.__ultima = None
        self.__total_de_elementos = 0
   
    def adicionar_comeco(self, professor):
        nova_celula = Celula()
        nova_celula.elemento = professor
        nova_celula.prioridade = professor.tempo_de_ifce
        
        nova_celula.proxima = self.__primeira #nova_celula aponta para primeira
        self.__primeira = nova_celula #nova_celula se torna a primeira da lista
 
        self.__total_de_elementos += 1

    def adicionar_posicao(self, posicao, professor):
        if posicao == 0:
            self.adicionar_comeco(professor)
        elif posicao >= self.__total_de_elementos:
            self.adicionar_fim(professor)
        else:
            nova_celula = Celula() 
            nova_celula.elemento = professor
            nova_celula.prioridade = professor.tempo_de_ifce

            anterior = self.__primeira

            for i in range(0, posicao-1):
                anterior = anterior.proxima
        
            nova_celula.proxima = anterior.proxima #nova_celula aponta para a proxima da anterior
            anterior.proxima = nova_celula #celula anterior aponta para nova_celula

            self.__total_de_elementos += 1
 
    def adicionar_fim(self, professor):
        if self.__total_de_elementos == 0:
            self.adicionar_comeco(professor)
        else:
            nova_celula = Celula()
            nova_celula.elemento = professor
            nova_celula.prioridade = professor.tempo_de_ifce

            atual = self.__primeira

            while atual.proxima != None:
                atual = atual.proxima

            nova_celula.proxima = atual.proxima #nova_celula aponta para o fim da lista
            atual.proxima = nova_celula #atual aponta para nova_celula
            
            self.__total_de_elementos += 1
 
    def pegar(self, posicao):
        if posicao < 0 or posicao >= self.__total_de_elementos:
            raise Exception("Posicao invalida!")
 
        atual = self.__primeira
 
        for i in range(0, posicao):
            atual = atual.proxima
        return atual.elemento
        
    def remover_comeco(self):
        self.__primeira = self.__primeira.proxima #a proxima da primeira se torna a primeira da lista
        self.__total_de_elementos -= 1

    def remover_posicao(self, posicao):
        if posicao == 0:
            self.remover_comeco()
        elif posicao == self.__total_de_elementos-1:
            self.remover_fim(professor)
        elif posicao >= self.__total_de_elementos:
            print('Posicao invalida!')
        else:
            anterior = self.__primeira

            for i in range(0, posicao-1):
                anterior = anterior.proxima

            anterior.proxima = anterior.proxima.proxima #a celula anterior aponta para a proxima da celula removida
            
            self.__total_de_elementos -= 1
        
    def remover_fim(self):
        atual = self.__primeira

        while atual.proxima.proxima != None: #loop para encontrar a penultima celula
            atual = atual.proxima

        atual.proxima = None #penultima celula aponta para None

        self.__total_de_elementos -= 1
        
    def remover_elemento(self, professor):
        atual = self.__primeira

        if atual.elemento == professor:
            self.remover_comeco()
        else:
            while atual.proxima != None:
                if atual.proxima.elemento == professor:
                    atual.proxima = atual.proxima.proxima #celula atual aponta para a proxima da celula removida
                    break
                atual = atual.proxima

            self.__total_de_elementos -= 1

    def remover_todos_elementos(self, professor):
        atual = self.__primeira

        if atual.elemento == professor:
            self.remover_comeco()
        
        while atual.proxima != None:
            if atual.proxima.elemento == professor:
                atual.proxima = atual.proxima.proxima 
                self.__total_de_elementos -= 1
            atual = atual.proxima

        if atual.proxima == self.__ultima and atual.elemento == professor:
            self.remover_fim()

    def contem(self, professor):
        atual = self.__primeira
        while atual != None:
            if atual.elemento == professor:
                return True
            atual = atual.proxima
        return False

    def tamanho(self):
        return self.__total_de_elementos

    def __str__(self):
        string_final = '['
        atual = self.__primeira
 
        if atual != None:
            string_final = string_final + atual.elemento.nome 
            atual = atual.proxima
            
            while atual != None:
                
                string_final = string_final + ', ' + atual.elemento.nome
                atual = atual.proxima
            
        string_final = string_final + ']'
        return string_final

        if self.__total_de_elementos == 0:
            return '[]'
