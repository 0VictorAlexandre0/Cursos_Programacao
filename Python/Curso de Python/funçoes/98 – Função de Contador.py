#Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def linha():
    print('-='*20)

def contagem(i, f, p):
    if p == 0:
        p = 1
    for i in range(i, f, p):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')
    linha()


linha()
print('Contagem de 1 até 10 de 1 em 1: ')
for i in range(1, 10+1, 1):
    print(i, end=' ')
    sleep(0.5)
print('FIM!')
linha()
print()

linha()
print('Contagem de 10 até 0 de 2 em 2: ')
for i in range(10, 0-1, -2):
    print(i, end=' ')
    sleep(0.5)
print('FIM!')
linha()
print()

linha()
print('Agora sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)



