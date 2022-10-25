class Celula:
    def __init__(self):
        self.proxima = None
        self.elemento = None
        self.prioridade = 0
 
    @property
    def proxima(self):
        return self._proxima
 
    @proxima.setter
    def proxima(self, proxima):
        self._proxima = proxima
 
    @property
    def elemento(self):
        return self._elemento

    @elemento.setter
    def elemento(self, elemento):
        self._elemento = elemento

    @property
    def prioridade(self):
        return self._prioridade

    @prioridade.setter
    def prioridade(self, prioridade):
        self._prioridade = prioridade

