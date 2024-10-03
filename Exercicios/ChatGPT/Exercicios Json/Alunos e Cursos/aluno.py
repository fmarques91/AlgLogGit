from curso import *

class Aluno:
    def __init__(self, nome, idade, curso = []):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        
        
    def showAluno(self):
        i = 0
        soma = 0
        print('Aluno: ', self.nome)
        print('Idade: ', self.idade)
        for curso in self.curso:
            curso.showCurso()
            soma += curso.nota
            i += 1
        print('-' * 20)
        print(f'Matriculado em um total de {i} cursos!')
        print(f'Media entre as matérias é: {soma / i}')
        
    def addCurso(self):
        while True:
            print('1) Cadastrar Curso\n0) Sair')
            opcao = input('Digite sua opção: ')
            if opcao == '0':
                break
            curso = Curso(input('Digite o Curso: '), float(input('Digite sua nota: ')))
            
            self.curso.append(curso)
            
    def to_dict(self):
        return {
            'nome': self.nome,
            'idade': self.idade,
            'curso': [iCurso.to_dict() for iCurso in self.curso]
        }