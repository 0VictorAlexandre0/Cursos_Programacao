from random import randint
from time import sleep

print('=-'*20)
print('{:^40}'.format(' Bem-vindo ao CASSINO HONESTO'))
print('=-'*20)
print('Aqui você vai apostar e vai ganhar hein, pode ter certeza...')
print('Vamos começar XD')
print('=-'*20)

vencedor = 0

saldo = int(input('Quanto de saldo você tem? R$'))
saldo_inicial = saldo

while True:
    if saldo <= 0:
        print('Você não possui saldo suficiente.')
        break

    aposta = int(input('Qual o valor que deseja apostar: R$'))
    while aposta <= 0:
        print('Tente novamente')
        aposta = int(input('Qual o valor que deseja apostar: R$'))
    if aposta > saldo:
        print('Você não pode apostar um valor maior que seu saldo.')
        break

    if aposta <= 100:
        dado = randint(0, 10)
        sorte = randint(0, 10)
    else:
        dado = randint(0, 10)
        sorte = randint(0, 25)

    if vencedor >= 3:
        dado = randint(0, 10)
        sorte = randint(0, 50)

    print('E você...')
    sleep(1.5)
    print('='*20)

    if dado == sorte:
        print('GANHOU!!!')
        saldo += aposta
        vencedor += 1
        print(f'Saldo restante R${saldo}')
    else:
        print('PERDEU!!! :P')
        saldo -= aposta
        print(f'Saldo restante R${saldo}')

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar == 'S':
            print('=-' * 20)

    if continuar == 'N':
        print('=-' * 20)
        saldo_final = saldo
        print(f'Você começou com R${saldo_inicial}')
        print(f'Ficou com R${saldo_final}')
        if saldo_final > saldo_inicial:
            saldo_ganho = saldo_final - saldo_inicial
            print(f'Teve ganho de R${saldo_ganho}')
        elif saldo_final < saldo_inicial:
            saldo_perda = saldo_inicial - saldo_final
            print(f'Teve perda de R${saldo_perda}')
        else:
            print('Seu saldo não mudou.')
        break
