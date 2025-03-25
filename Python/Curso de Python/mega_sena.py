#'''Faça um programa que ajude um jogador da Mega Sena
# a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para
# cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

print('-'*19)
print('     MEGA SENA     ')
print('-'*19)

lista = []
jogos = []
quantjogos = int(input('Quantos jogos você quer que eu sorteie? '))
total = 0

sleep(1)
while total <= quantjogos -1: #para gerar exatamente oq eu pedi
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista: #para os números não se repetirem.
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print()
print('=-'*3, f' SORTEANDO {quantjogos} JOGOS ', '-='*3)
sleep(1)
for item, lista in enumerate(jogos): #para cada elemento na lista de jogos
    print(f'Jogo {item+1}: {lista}')
    sleep(1)
print('=-'*5, 'BOA SORTE!', '-='*5)