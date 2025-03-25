#Crie um programa que leia o nome, ano de nascimento e carteira
#de trabalho e cadastre-os(com idade) em um dicionario se por
#acaso a CTPS for diferente de ZERO, o dicionário receberá também
#o ano de contratação e o salário. Calcule e acrescente, além da
#idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

funcionario = {}
funcionario['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
funcionario['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
funcionario['idade'] = datetime.now().year - nascimento

if funcionario['ctps'] != 0:
    funcionario['contratação'] = int(input('Ano de contratação: '))
    funcionario['salário'] = float(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['idade'] + ((funcionario['contratação'] + 35) - datetime.now().year)
print('-='*30)

for key, value in funcionario.items():
    print(f'- {key} = {value}')