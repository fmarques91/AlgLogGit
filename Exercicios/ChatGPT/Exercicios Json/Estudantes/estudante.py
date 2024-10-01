class Estudante:
    def __init__(self, nome, media):
        self.nome = nome
        self.media = media
        self.curso = []
        
    def showEstudante(self):
        print('*' * 10)
        print('Nome:', self.nome)
        print('Media:', self.media)
        print('Cursos:', ', '.join(self.curso))
        print('*' * 10)
        
    def addCurso(self, curso):
        self.curso.append(curso)

    def cadastrarCurso(self):
        while True:
            curso = input('Digite o curso ou "sair": ')
            if curso.upper() == 'SAIR':
                break
            self.addCurso(curso)