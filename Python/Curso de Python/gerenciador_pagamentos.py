#'''Elabore um programa que calcule o valor a ser pago
# por um produto, considerando seu preço normal e
# condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros'''

print('{:=^30}'.format(' LOLJA '))
#'''formatação do nome: {:^x}, '^' significa pra centralizar em X espaços
# '=' o simbolo que quis nesses espaços sobrando.'''

preço = float(input('Preço das compras: '))
print('''Escolha uma das formas de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opçao = int(input('Sua opção: '))
if opçao == 1:
    valor = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} ficará por R${:.2f} por conta do desconto de 10%'.format(preço, valor))
elif opçao == 2:
    valor = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} ficará por R${:.2f} por conta do desconto de 5%'.format(preço, valor))
elif opçao == 3:
    valor = preço / 2
    print('Sua compra de R${:.2f} ficará por 2 vezes de R${:.2f}'.format(preço, valor))
elif opçao == 4:
    parcela = int(input('Quantas vezes deseja parcelar? '))
    valor = preço + (preço * 20 / 100)
    valor_parcela = valor / parcela
    total = valor_parcela * parcela
    print('''Sua compra de R${:.2f} ficará por {} vezes de R${:.2f} por conta do juros de 20%.
No total ficará por R${:.2f}'''.format(preço, parcela, valor_parcela, total))


