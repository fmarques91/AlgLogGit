from curso import *

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.curso = []
        
        
    def showAluno(self):
        print('=' * 20)
        print('Aluno: ', self.nome)
        print('Idade: ', self.idade)
        for curso in self.curso:
            self.showCurso()
        print('=' * 20)
        
    def addCurso(self):
        while True:
            print('1) Cadastrar Curso\n0) Sair')
            opcao = input('Digite sua opção: ')
            if opcao == 0:
                break
            curso = Curso(input('Digite o Curso: '), float(input('Digite sua nota: ')))
            
            self.curso.append(curso)