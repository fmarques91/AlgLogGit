from tarefa import Tarefa, concluirTarefa, listarTodos, listarTarefas

bdTarefas = []

while True:
    opcao = int(input('"OPÇÕES"\n1) Incluir uma nova tarefa. \n2) Marcar tarefa como concluida. \n3) Listar tarefas.\n4) Sair.\nDigite sua opção: '))

    if opcao == 1:
        tarefaInclusao = Tarefa(input('Digite o nome da sua tarefa: '), input('Digite a descrição da sua tarefa: '))
        bdTarefas.append(tarefaInclusao)
    elif opcao == 2:
        concluirTarefa(bdTarefas)
    elif opcao == 3:
        while True:
            print('-' * 5, 'OPÇÕES', '-' * 5)
            print('1) Filtrar por concluídos.\n2) Filtrar por pendentes.\n3) Listar todos\n4) Sair.')
            opcao2 = int(input('Digite sua opção: '))
            if opcao2 == 4:
                break
            else:
                listarTarefas(opcao2, bdTarefas)
    elif opcao == 4:
        break
    else:
        print('\nDigite uma opção válida!\n')