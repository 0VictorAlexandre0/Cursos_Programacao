#'''Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação
# mensal, não pode exceder a 30% do salário ou então o empréstimo
# será negago.'''

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))

prestaçao = casa / (anos * 12)
#prestação é por mês, logo multiplica a quantidade de anos em 12 e depois divide pelo valor da casa

excedente = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestaçao))
if prestaçao <= excedente:
    print('Empréstimo concedido.')
else:
    print('Empréstimo negado.')


