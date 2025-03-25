#'''Crie um programa que tenha uma tupla única com
# nome de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando
# os dados de forma tabular.'''

lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidos', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.90,
         'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>7.2f}')
print('-'*40)
