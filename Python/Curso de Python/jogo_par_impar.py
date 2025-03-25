#'''Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final
# do jogo.'''

from random import randint

cont = 0

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

while True:
    n = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = n + computador
    escolha = ' ' #equivale a 0/nulo numa conta, só que em string.

    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
        print('-' * 30)

    print(f'Você jogou {n} e o computador jogou {computador}. Total de {soma}, ', end='')
    print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')
    print('-' * 30)
    if escolha == 'P':
        if soma % 2 == 0:
            cont += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            print('=-' * 15)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            print('=-' * 15)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            break
    print('Vamos jogar novamente...')
    print('=-' * 15)
