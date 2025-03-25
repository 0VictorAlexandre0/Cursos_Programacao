#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = {}

jogador['nome'] = input('Nome do jogador: ')
total = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

partidas = []
for i in range(0, total):
    partidas.append(int(input(f'    Quantos gols na partida {i+1}: ')))
jogador['gols'] = partidas[:]

jogador['total'] = sum(partidas)

print('-='*30)

for key, value in jogador.items():
    print(f'{key} = {value}')
print('-='*30)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')
for i, value in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {value} gols.')
print(f'Foi um total de {jogador['total']} gols.')