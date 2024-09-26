class Tarefa:
    #Atribuir um valor para caso não seja passado algum atributo. Para isso é necessário já existir um valor padrão.
    def __init__(self, titulo = 'Não preenchido', descricao = 'Não preenchido', status = 'Pendente'):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def listar(self):
        print('-' * 5, self.titulo, '-' * 5)
        print('Descrição da tarefa: ', self.descricao)
        print('Status: ', self.status)

def listarTodos(lista):
    for i in range(len(lista)):
        print('\n', i + 1, ')')
        lista[i].listar()


def concluirTarefa(lista):
    listarTodos(lista)
    opcao = int(input('\nQual das tarefas deseja marcar como concluida? '))
    try:
        lista[opcao - 1].status = 'Concluído'
        listarTodos(lista)
        print('-' * 30)
    except IndexError:
        print('\nDigite uma opção válida!\n')


def listarTarefas(opcao2, bdTarefas):
    if opcao2 == 1:
        print('\n')
        for taref in bdTarefas:
            if taref.status == 'Concluído':
                taref.listar()
                print('*' * 100)
                print('\n')
    elif opcao2 == 2:
        print('\n')
        for taref in bdTarefas:
            if taref.status == 'Pendente':
                taref.listar()
                print('*' * 100)
        print('\n')
    elif opcao2 == 3:
        listarTodos(bdTarefas)
        print('\n')
    else:
        print('Digite uma opção válida!')