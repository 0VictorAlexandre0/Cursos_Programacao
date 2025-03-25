# Adapte o código do desafio #107, criando uma função adicional
# chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco, 'US$')} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de R${moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumento de 10%, temos R${moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 15%, temos R${moeda.moeda(moeda.diminuir(preco,15))}')



