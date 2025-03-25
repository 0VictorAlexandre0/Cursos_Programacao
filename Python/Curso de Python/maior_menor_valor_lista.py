#'''Faça um programa que leia 5 valores numéricos e guarde - os
# em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e suas respectivas posições na lista.'''

valores = []
maior = menor = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
    #atribuindo 5 valores na lista
    if pos == 0: #o 1º valor estará na posição maior quanto menor
        maior = menor = valores[pos]
    else:
        if valores[pos] > maior: #se os valores na posição tal for maior que o 1º número ele vira o maior
            maior = valores[pos]
        if valores[pos] < menor: #se os valores na posição tal for menor que o 1º número ele vira o menor
            menor = valores[pos]
print('=-'*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
#agora preciso percorrer minha lista para achar a posição dos valores:
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{pos}. ', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}. ', end='')

#'''OBSERVAÇÕES:
# talvez funcionasse esse código:
# print(f'O maior valor digitado foi {max()} na posição {}')
# print(f'O menor valor digitado foi {min()} na posição {}')
#
# E as variáveis POS, não se afetam, pois estão em posições e
# lugares diferentes.'''
