dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
pagar = (dias * 60) + (km * 0.15)
print('O total a ser pago é de R${:.2f}'.format(pagar))