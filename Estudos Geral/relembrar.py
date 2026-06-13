'''tarefas = []

tarefas.append("Estudar")
tarefas.append("Comer")
tarefas.append("Dormir")

for item in tarefas:
    print(item)'''


opcao = ""

while opcao != "3":
    print("1 - Adicionar tarefa")
    print('2 Listar tarefas')
    print('3 - Sair')

    opcao = input("Escolha: ")

if opcao == "1":
    

tarefas = []

nova_tarefa = input("Qual nova tarefa? ")
tarefas.append(nova_tarefa)
print(tarefas)













