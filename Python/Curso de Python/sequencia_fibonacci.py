 #'''Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência.
# 0 1 1 2 3 5 8'''

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

n = int(input('Quantos termos você quer mostrar? '))
termo1 = 0 #sempre começa com 0 e 1
termo2 = 1

print('~'*30)
print('{} -> {}'.format(termo1, termo2), end='')
#já faz a formatação dos 2 termos.

cont = 3 #começa em 3 por conta que é a partir do 3º termo
while cont <= n:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')
    #'''abaixo os termos irão caminhar pela sequência assumindo o lugar do anterior(t1 e t2)
    # e o posterior (t3) será o novo número da sequencia.
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' -> Fim')
print('~'*30)