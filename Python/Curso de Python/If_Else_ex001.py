#"""Eescreva um programa que faça o computador 'pensar' em
# um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu."""

import random

numero = int(input('Digite um número de 0 a 5: '))
if numero <= -1 or numero >= 6:
    numero = int(input('Digite novamente: '))
lista = [0 ,1, 2, 3, 4, 5]
escolhido = random.choice(lista)
if escolhido == numero:
    print('O número digitado foi {} e o número escolhido foi {}, você venceu!'.format(numero, escolhido))
else:
    print('O número digitado foi {} e o número escolhido foi {}, você perdeu!'.format(numero, escolhido))

#Guanabara code:

from random import randint
from time import sleep #fazer o pc esperar algusn segundos

computador = randint(0, 5) #faz o pc pensar/sortear
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3) #esperar 3 segundos com o print acima
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))


