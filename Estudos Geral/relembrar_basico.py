'''tarefas = []

tarefas.append("Estudar")
tarefas.append("Comer")
tarefas.append("Dormir")

for item in tarefas:
    print(item)'''


opcao = ""
tarefas = []

while opcao != "0":
    print()
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Remover tarefa')
    print('0 - Sair')
    print()

    opcao = input("Escolha: ")
    print()

    if opcao == "1":
        nova_tarefa = input("Qual nova tarefa? ")
        print()
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for numero, tarefa in enumerate(tarefas, start=1):
                print(f"{numero}. {tarefa}")

    elif opcao == '3':
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for numero, tarefa in enumerate(tarefas, start=1):
                    print(f"{numero}. {tarefa}")
            print()
                  
            remover = int(input('Qual tarefa você quer remover? '))

            if 1 <= remover <= len(tarefas):
                tarefas.pop(remover - 1)
                print('Tarefa removida')
            else:
                print("Número inválido")

    elif opcao == "0":
        print('Agradeço por usar')
        break

    else:
        print('tente novamente')

        













