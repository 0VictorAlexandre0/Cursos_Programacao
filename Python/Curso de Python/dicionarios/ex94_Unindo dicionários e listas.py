#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
from operator import truediv


galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')

    while True:
        pessoa['sexo'] = input('Sexo (M/F): ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite novamente.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resposta = input('Quer continuar? (S/N)' ).upper()[0]
        if resposta in 'SN':
            break
        print('Digite novamente.')
    if resposta == 'S':
        break
print('-='*30)

print(f'Ao todo temos {len(galera)} pessoas cadastradas.')

media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')

print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']} ', end='')

print('Lista das pessoas acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for key, value in p.items():
            print(f'{key} = {value}; ', end='')
        print()
        
print('FIM')