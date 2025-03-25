# Modifique as funções que form criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco, 'US$')} é {moeda.metade(preco, True)}')
print(f'O dobro de R${moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumento de 10%, temos R${moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 15%, temos R${moeda.diminuir(preco,15, True)}')


