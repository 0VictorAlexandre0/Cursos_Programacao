#'''Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final,
# mostre:
# - Qual é o total gasto na compra.
# - Quantos produtos custam mais de R$1000.
# - Qual é o nome do produto mais barato.'''

print('-'*30)
print('Loja'.center(30))
print('-'*30)

soma = cont = 0
menorpreço = contmenor = 0
barato = ' '

while True:
    produto = input('Nome do Produto: ')
    preço = int(input('Preço: R$'))
    soma += preço
    contmenor += 1
    if preço > 1000:
        cont += 1

    if contmenor == 1: #contador de produtos
        menorpreço = preço
        barato = produto
    else:
        if preço < menorpreço:
            menorpreço = preço
            barato = produto
    #'''ou if contmenor == 1 or preço < menorpreço
    #       menorpreço = preço
    #       barato = produto'''

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        print('-'*10, end='')
        print(' Fim do Programa ', end='')
        print('-' * 10)
        #print('{:-^30}'.format(' Fim do programa ')) forma certa
        break
    else:
        print('-'*30)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menorpreço:.2f}')
