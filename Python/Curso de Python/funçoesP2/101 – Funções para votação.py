#Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(nasc):
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade <= 17:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 18 <= idade <= 64:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'

print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

