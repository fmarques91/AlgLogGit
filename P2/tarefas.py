def status():
    while True:
        print('=-' * 20)
        print('Defina o status da tarefa')
        print('1) Pedente')
        print('2) Em Progresso')
        print('3) Concluído')
        opcao = int(input('Digite o número correpondente ao status: '))
        print('=-' * 20)

        if opcao == 1:
            return 'Pendente'
        elif opcao == 2:
            return 'Em Progresso'
        elif opcao == 3:
            return 'Concluído'
        else:
            print('Digite uma opção válida!')

def showTarefas(tarefas):
    print('=-' * 40)
    for tarefa in tarefas:
        print(f'Título: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\nPrazo: {tarefa['prazo']} dias\nStatus: {tarefa['status']}')
        print('=-' * 40)

def filtrarTarefa(tarefas, filtro, tipoFiltro):
    if tipoFiltro == 1:
        for tarefa in tarefas:
            if tarefa['prazo'] > filtro:
                print('=-' * 40)
                print(f'Título: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\nPrazo: {tarefa['prazo']} dias\nStatus: {tarefa['status']}')
                print('=-' * 40)
    elif tipoFiltro == 2:
        for tarefa in tarefas:
            if tarefa['prazo'] < filtro:
                print('=-' * 40)
                print(f'Título: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\nPrazo: {tarefa['prazo']} dias\nStatus: {tarefa['status']}')
                print('=-' * 40)
    elif tipoFiltro ==3:
        for tarefa in tarefas:
            if tarefa['prazo'] == filtro:
                print('=-' * 40)
                print(f'Título: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\nPrazo: {tarefa['prazo']} dias\nStatus: {tarefa['status']}')
                print('=-' * 40)

tarefas = [{"titulo": "Levantamento", "descricao": "Levamento de requisitos para construção do Projeto", "prazo" : 8, "status": "Concluído"}, 
           {"titulo": "Protóripo", "descricao": "Criação de protótipo para apresentação ao cliente", "prazo" : 5, "status": "Concluído"}, 
           {"titulo": "Validação", "descricao": "Validação do protótipo com o cliente", "prazo" : 10, "status": "Concluído"}, 
           {"titulo": "Escopo desenvolvimento", "descricao": "Realizar o escopo para desenvolvimento, criação de diagramas e algorítmos", "prazo" : 11, "status": "Concluído"}, 
           {"titulo": "Desenvolvimento", "descricao": "Realizar o desenvolvimento do código em Python", "prazo" : 5, "status": "Pendente"}]

opcao = None
while opcao != 0:
    print('Gerenciador de Tarefas')
    print('1) Adicionar uma nova Tarefa')
    print('2) Concluir Tarefa')
    print('3) Filtrar Tarefa por prazo')
    print('4) Editar Tarefas')
    print('0) Sair')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        novaTarefa = {
            'titulo' : input('Digite o nome para sua nova tarefa: '),
            'descricao' : input('Digite a descrição da tarefa: '),
            'prazo' : int(input('Digite o prazo em dias: ')),
            'status' : status()
        }
        tarefas.append(novaTarefa)

    elif opcao == 2:
        showTarefas(tarefas)

        concluirTarefa = input('Digite o título da tarefa a ser alterada o status: ')

        for tarefa in tarefas:
            if tarefa['titulo'].lower() == concluirTarefa.lower():
                tarefa['status'] = status()
                break
        else:
            print('Tarefa não encontrada')

    elif opcao == 3:
        filtro = int(input('Digite o número para filtrar os prazos: '))

        print('=-' * 20)
        print('Defina como deseja filtrar:')
        print(f'1) Maior que {filtro}')
        print(f'2) Menor que {filtro}')
        print(f'3) Igual a {filtro}')
        tipoFiltro = int(input('Digite a número correpondente ao tipo de filtro: '))
        print('=-' * 20)

        filtrarTarefa(tarefas, filtro, tipoFiltro)

    elif opcao == 4:
        showTarefas(tarefas)

        editarTarefa = input('Qual tarefa deseja editar: ')

        for tarefa in tarefas:
            if tarefa['titulo'].lower() == editarTarefa.lower():
                print('=-' * 40)
                print('Opção Para Edição')
                print('1) Título')
                print('2) Descrição')
                print('3) Prazo')
                print('4) Status')
                paraEditar = int(input('Digite a opção conrrepondente para editar o campo: '))
                print('=-' * 40)

                if paraEditar == 1:
                    tarefa['titulo'] = input('Digite o novo título: ')
                    break
                elif paraEditar == 2:
                    tarefa['descricao'] = input('Digite a nova descrição: ')
                    break
                elif paraEditar == 3:
                    tarefa['prazo'] = int(input('Digite o novo prazo: '))
                    break
                elif paraEditar == 4:
                    tarefa['status'] = status()
                    break
                else:
                    print('Opção não válida!')
                    break
        else:
            print('Tarefa não encontra')