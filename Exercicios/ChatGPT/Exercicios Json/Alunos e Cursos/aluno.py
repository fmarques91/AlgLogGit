from curso import *

class Aluno:
    def __init__(self, nome, idade, curso = []):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        
        
    def showAluno(self):
        print('=' * 20)
        print('Aluno: ', self.nome)
        print('Idade: ', self.idade)
        print('Curso: ', self.curso.nomeCurso)
        print('Nota: ', self.curso.nota)
        print('=' * 20)