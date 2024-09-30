class Estudante:
    def __init__(self, nome, media):
        self.nome = nome
        self.media = media
        
    def showEstudante(self):
        print('Nome:', self.nome)
        print('Media:', self.media)
    