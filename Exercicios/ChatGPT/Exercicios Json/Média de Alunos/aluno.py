class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        
    def showAluno(self):
        print('=' * 20)
        print('Aluno: ', self.nome)
        print('Idade: ', self.idade)
        print('Nota : ', self.nota)
        print('=' * 20)