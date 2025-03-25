preço = float(input('Qual é o preço do produto? R$: '))
novo = preço - (preço * 5 / 100) # -> dentro das() equivale a 5% toda essa conta
#novo preço é igual o preço antigo menos 5%
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))

