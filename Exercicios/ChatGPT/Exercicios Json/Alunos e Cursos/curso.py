class Curso:
    def __init__(self, nomeCurso, nota):
        self.nomeCurso = nomeCurso
        self.nota = nota
        
    def showCurso(self):
        print('=' * 5)
        print('*' * 5, 'CURSO', '*' * 5)
        print('Curso: ', self.nomeCurso)
        print('Nota: ', self.nota)
        print('=' * 5)