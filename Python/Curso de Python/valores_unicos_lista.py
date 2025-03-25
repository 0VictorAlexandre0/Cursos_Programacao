#'''Crie um programa onde o usuário possa digitar vários
# valores numéricos e cadastre - os em uma lista. Caso o
# número já existe lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.'''

lista = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Digite novamente...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print('=-'*20)
lista.sort()
print(f'Você digitou os valores {lista}') #ou {sorted(lista)}')
