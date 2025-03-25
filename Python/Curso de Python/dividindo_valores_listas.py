lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'Lista completa {lista}')
for item, numero in enumerate(lista): #percorrer itens da lista
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impares.append(numero)
print(f'Lista de pares {pares}')
print(f'Lista de ímpares {impares}')
