#'''Desenvolva um programa que leia 6 números inteiros e
# mostre a soma apenas dos pares, se for ímpar, desconsidere-o.'''

soma = 0
cont = 0
for vezes in range(1, 7):
    num = int(input('Digite o {} valor: '.format(vezes)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))

