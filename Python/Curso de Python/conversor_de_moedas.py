real = float(input('Quanto de dinheiro você tem? R$:'))
dolar = real / 5.27
euro = real / 5.61
print('Com R${:.2f} você pode comprar US${:.2}'.format(real,dolar))
print('Com R${:.2f} você pode comprar E{:.2f}'.format(real,euro))
