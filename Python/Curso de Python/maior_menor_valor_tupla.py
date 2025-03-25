#'''Crie um programa que vai gerar 5 números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior
# valor que estão na tupla.'''

from random import randint

aleatorio = (randint(0, 10), randint(0, 10), randint(0, 10),
             randint(0, 10), randint(0, 10))
#print(f'Os valores sorteados foram: {aleatorio}') aparece ()
print('Os valores sorteados foram: ', end='')
for i in aleatorio:
    print(f'{i} ', end='') #sem ()
print(f'\nO maior valor sorteado foi {max(aleatorio)}') #método mais facil
print(f'O menor valor sorteado foi {min(aleatorio)}')


