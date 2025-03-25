# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando os 5 valores: ',end='')
    sleep(1)
    for i in range(5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print('Pronto!')


def somaPar(lista):
    cont = 0
    for i in numeros:
        if i % 2 == 0:
            cont += i
    print(f'Somando os valores pares de {numeros}, temos {cont}')


numeros = []
sorteia(numeros)
sleep(1.5)
somaPar(numeros)

