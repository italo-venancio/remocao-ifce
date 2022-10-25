from fila_de_prioridade import Fila_de_prioridade
from professor import Professor
from listaLigada import ListaLigada

def teste_fila():
    prof01 = Professor(nome='Joe', matricula=1234, subarea='Botanica', campus_atual='Jaguaribe', campus_removido='Fortaleza', tempo_de_ifce=30, idade=27, nota_concurso=9.2)
    prof02 = Professor(nome='Lu', matricula=2345, subarea='Zoologia', campus_atual='Jaguaribe', campus_removido='Fortaleza', tempo_de_ifce=60, idade=29, nota_concurso=9.5)
    prof03 = Professor(nome='Will', matricula=3456, subarea='Citologia', campus_atual='Jaguaribe', campus_removido='Fortaleza', tempo_de_ifce=35, idade=28, nota_concurso=8.6)
    prof04 = Professor(nome='Beth', matricula=4567, subarea='Citologia', campus_atual='Jaguaribe', campus_removido='Fortaleza', tempo_de_ifce=40, idade=25, nota_concurso=8.7)
    prof05 = Professor(nome='Nair', matricula=5678, subarea='Citologia', campus_atual='Jaguaribe', campus_removido='Fortaleza', tempo_de_ifce=90, idade=30, nota_concurso=9.7)
    fila = Fila_de_prioridade()
    print(fila.empty())

    fila.push(prof01)
    print(fila)
    fila.push(prof02)
    print(fila)
    fila.push(prof03)
    print(fila)
    fila.push(prof04)
    print(fila)
    fila.push(prof05)
    print(fila)

    fila.pop()
    print(fila)
    
    print(fila.empty())

if __name__ == '__main__':
    teste_fila()