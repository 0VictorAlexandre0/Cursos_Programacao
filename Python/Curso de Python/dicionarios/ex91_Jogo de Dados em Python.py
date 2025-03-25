#Crie um programa onde 4 jogadores joguem um dado e
#tenham resultados aleatórios. Guarde esses resultados
#em um dicionário. No final, coloque esse dicionário
#em ordem, sabendo que o vencedor tirou o maior número
#no dado.

from random import randint
from time import sleep

from operator import itemgetter
#Nesse caso, a função itemgetter(1) é utilizada como argumento da função sorted(),
#o que indica que a ordenação deve ser feita com base no valor do dicionário, e não na chave.

jogadores = {
    'jogador 1' : randint(1, 6),
    'jogador 2' : randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6),
}

print('Valores sorteados:')
for key, value in jogadores.items():
    print(f'{key}: {value}')
    sleep(1)

print('-='*30)

#crie uma lita para ordenar, pode ser na tupla, mas ainda nn sei fazer

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#criando lista ordenada com base nos itens de jogadores e colocando em ordem maior pro menor

print('  == RANKING DOS JOGADORES ==')
sleep(1)
for indice, values in enumerate(ranking):
    print(f'{indice+1}º lugar: {values[0]} com {values[1]}')
    sleep(1)