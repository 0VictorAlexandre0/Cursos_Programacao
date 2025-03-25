#'''Escreva um programa que leia dois numeros inteiros e compare-os,
# mostrando na tela uma mensagem:
# - o primeiro é maior
# - o segundo é maior
# - os dois são iguais'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo número é maior.')
else:
    print('Não existe número maior, os dois são iguais.')

    