class Professor:
    def __init__(self, nome, matricula, subarea, campus_atual, campus_removido, tempo_de_ifce, idade, nota_concurso):
        self.nome = nome #string
        self.matricula = matricula #inteiro
        self.subarea = subarea #string
        self.campus_atual = campus_atual #string
        self.campus_removido = campus_removido #string
        self.tempo_de_ifce = tempo_de_ifce #inteiro 
        self.idade = idade #inteiro
        self.nota_concurso = nota_concurso #float

    @property 
    def tempo_de_ifce(self):
        return self._tempo_de_ifce

    @tempo_de_ifce.setter
    def tempo_de_ifce(self, valor):
        self._tempo_de_ifce = valor

    def __str__(self):
        return self.nome



        