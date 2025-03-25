#'''Faça um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria de acordo com a idade.'''

from datetime import date

atual = date.today().year #pegar ano atual
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc #idade é igual o ano atual menos o nascimento
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')

