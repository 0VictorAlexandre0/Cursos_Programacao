#'''Crie uma tupla preenchida com os 10 primeiros colocados
# de um campeonato de futebol na ordem de colocação. Depois mostre:
# - OS 5 PRIMEIROS
# - ÚLTIMOS 4
# - TIMES EM ORDEM ALFABÉTICA
# - POSIÇÃO DO BRASIL'''

tupla = ('Estados Unidos', 'Japão', 'Brasil', 'França', 'China', 'Egito', 'Argentina', 'Coreia', 'Chile', 'Grécia')

print('-='*15)
print(f'Lista de times: {tupla}')
print('-='*15)
print(f'Os 5 primeiros: {tupla[0:5]}')
print('-='*15)
print(f'Os últimos 4: {tupla[6:10]}') #ou [-4:]
print('-='*15)
print(f'Em ordem alfabética: {sorted(tupla)}')
print('-='*15)
print(f'O Brasil está na {tupla.index('Brasil')+1}ª posição.')
#index para pesquisar tal coisa numa tupla, +1 porque começa em 0.
