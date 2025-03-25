#Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    cont = maior = 0
    print('Analisando os valores...')
    sleep(3)

    for i in num:
        print(f'{i}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(f'\nForam informados {cont} valores')
    print(f'O maior valor foi {maior}')
    print()

maior(1,2,3,4,5)
maior(8,5,3,7,0,6,4,1,2,4,5,7,9,0)

