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

def linha(tamanho = 42):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc