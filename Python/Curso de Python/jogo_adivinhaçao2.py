from random import randint

computador = randint(1, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('\nQual seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas!'.format(tentativas))
