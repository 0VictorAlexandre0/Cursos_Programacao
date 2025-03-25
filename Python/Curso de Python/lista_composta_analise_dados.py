#'''Faça um programa que leia o nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# - Quanto pessoas foram cadastrados.
# - Uma listagem com as pessoas mais pesadas.
# - Uma listagem com as pessoas mais leves.'''

listatemporaria = []
listaprincipal = []
maior = menor = 0

while True:
    listatemporaria.append(input('Nome: ')) #posição 0
    listatemporaria.append(float(input('Peso: '))) #posição 1

    if len(listaprincipal) == 0: #se não tiver ninguém na lista2
        maior = menor = listatemporaria[1] #pegar apenas o peso
    else:
        if listatemporaria[1] > maior:
            maior = listatemporaria[1]
        if listatemporaria[1] < menor:
            menor = listatemporaria[1]

    listaprincipal.append(listatemporaria[:]) # [:] é pegar uma cópia, e não uma ligação.
    listatemporaria.clear() #para sempre ir adicionando novos na lista1 e lista2 copia a 1.

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'Os dados foram {listaprincipal}')
print(f'Ao todo você cadastrou {len(listaprincipal)} pessoas.')
#poderia criar um cont, mas apenas pedi o tamanho da lista2, com todos os cadastros.

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoa in listaprincipal:
    if pessoa[1] == maior: #para cada pessoa que estiver em posição 1(peso)
        print(f'[{pessoa[0]}]') #mostra nome da pessoa em posição 0(nome)
print(f'O menor peso foi de {menor}Kg. Peso de ',end='')
for pessoa in listaprincipal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]')
        