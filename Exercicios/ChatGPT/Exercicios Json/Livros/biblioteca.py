import json

class Livro():
    def __init__(self, titulo, autor, anoPubli, genero):
        self.titulo = titulo
        self.autor = autor
        self.anoPubli = anoPubli
        self.genero = genero
        
    def showLivro(self):
        print('\nTitulo: ', self.titulo)
        print('Autor: ', self.autor)
        print('Publicação: ', self.anoPubli)
        print('Gênero: ', self.genero, '\n')
        
def salvarLivros(bdLivro, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump([livro.__dict__ for livro in bdLivro], f, ensure_ascii=False)
        
def carregarLivros(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            livro_json = json.load(f)
            return [Livro(l['titulo'], l['autor'], l['anoPubli'], l['genero']) for l in livro_json]
    except FileNotFoundError:
        return []

bdLivro = carregarLivros('bdLivro.json')

while True:
    print('*' * 5, 'CADASTRO DE LIVRO', '*' * 5)
    print('DIGITE 1 PARA CADASTRAR UM NOVO LIVRO.')
    print('DIGITE 2 PARA LISTAR.')
    print('DIGITE 0 PARA SAIR!')
    opcao = int(input('Opção: '))
    
    if opcao == 0:
        break
    elif opcao == 1:
        livro = Livro(input('Título do livro: '), input('Nome do Autor: '), input('Ano de Publicação: '), input('Gênero: '))
        bdLivro.append(livro)
        print('*' * 5, 'CADASTRADO', '*' * 5)
        livro.showLivro()
    elif opcao == 2:
        for listar in bdLivro:
            listar.showLivro()
    else:
        print('Digite uma opção válida!')
    
salvarLivros(bdLivro, 'bdLivro.json')    