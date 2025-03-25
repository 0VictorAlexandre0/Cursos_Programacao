#Faça o PC jogar Jokenpô com você

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

pc = randint(0, 2) #jogar entre os itens 0, 1 e 2
jogador = int(input('Qual sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 12)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)

if pc == 0: #pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('Você perdeu!')
    else:
        print('Jogada inválida!')

elif pc == 1: # papel
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você venceu!')
    else:
        print('Jogada inválida!')

elif pc == 2: #tesoura
    if jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')