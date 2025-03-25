#'''Crie um programa que vai ler vários números e colocar em
# uma lista. Depois disso, mostre:
# - Quantos números foram digitados.
# - A lista de valores, ordenada de forma decrescente.
# - Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print('O número 5 não está na lista.')
else:
    print('O número 5 está na lista.')
