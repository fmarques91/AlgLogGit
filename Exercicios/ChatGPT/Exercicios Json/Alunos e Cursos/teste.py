class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

# Criando um objeto de Endereco
meu_endereco = Endereco("Rua das Flores", "Cidade Maravilhosa")

# Criando um objeto de Pessoa que contém o objeto Endereco
pessoa = Pessoa("João", 30, meu_endereco)

# Usando print() para mostrar a estrutura
print(pessoa.nome)
print(pessoa.idade)
print(pessoa.endereco.rua)
print(pessoa.endereco.cidade)