class Curso:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        
    def showCurso(self):
        print('=' * 5)
        print('*' * 5, 'CURSO', '*' * 5)
        print('Curso: ', self.nome)
        print('Nota: ', self.nota)
        print('=' * 5)