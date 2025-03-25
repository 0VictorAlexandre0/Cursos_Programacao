#'''Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.'''

from datetime import date

atual = date.today().year

menor = 0
maior = 0

for i in range(1, 8):
    nascimento = int(input('Em que ano a {}º pessoa nasceu? '.format(i)))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('{} pessoas são maiores de idade.'.format(maior))
print('{} pessoas menores de idade.'.format(menor))