#'''Crie um programa onde o usuário possa digitar sete
# valores numéricos e cadastre-os em uma lista única que
# mantenha separados em valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.'''

listas = [[], []] #estou declarando 1 lista com 2 listas internas.
valores = 0
for i in range(1, 8):
    valores = int(input(f'Digite o {i}º valor: '))
    #não peguei os valores direto na lista pois vou pegar e depois separar, por isso fiz isso:
    if valores % 2 == 0:
        listas[0].append(valores)
    else:
        listas[1].append(valores)
print('-='*20)
listas[0].sort()
listas[1].sort()
print(f'Os valores pares digitados foram: {listas[0]}')
print(f'Os valores ímpares digitados foram: {listas[1]}')
