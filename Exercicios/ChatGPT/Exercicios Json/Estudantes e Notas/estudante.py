class Estudante:
    def __init__(self, nome, idade, nota = None, media = 0.0):
        self.nome = nome
        self.idade = idade
        self.nota = nota if nota is not None else []
        self.media = media
        
    def show_estudante(self):
        print('=-' * 20)
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Nota: {self.nota}')
        print(f'Média: {self.media:.1f}')
        
    def cadastrar_nota(self):
        while True:
            notas = float(input('Digite uma nota ou digite algum número negativo para SAIR: '))
            if notas < 0:
                self.media = sum(self.nota) / len(self.nota)
                break
            elif 0 <= notas <=10:
                self.nota.append(notas)
            else:
                print('Digite uma opção válida!')
        
    def to_dict(self):
        return{
            'nome': self.nome,
            'idade': self.idade,
            'nota': self.nota,
            'media': self.media            
        }
        
def filtrar_estudante(bdEstudante, media):
    media_acima = []
    for est in bdEstudante:
        if est.media >= media:
            media_acima.append(est)
    return media_acima