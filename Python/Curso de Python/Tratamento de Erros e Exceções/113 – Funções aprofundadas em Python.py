#Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função
# leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um número valido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o número')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um número valido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o número')
            return 0
        else:
            return n


num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')