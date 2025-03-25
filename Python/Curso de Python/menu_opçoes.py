#'''Crie um programa que leia 2 valores e mostre um menu.
# Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n1 = int(input('Digite o Primeiro valor: '))
n2 = int(input('Digite o Segundo valor: '))
sleep(0.5)
opçao = 0

while opçao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opçao = int(input('>>> Qual é a sua opção? '))

    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
        sleep(2)
    elif opçao == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} * {} é {}'.format(n1, n2, multiplicar))
        sleep(2)
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        sleep(2)
    elif opçao == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(2)
    elif opçao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa. Volte sempre!')
