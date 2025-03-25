#'''Crie um programa que simule o funcionamento de um caixa
# eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado e o programa vai informar quantas cédulas de
# cada valor serão entregues
# OBS: Considere que o caixa eletrônico possui cédulas de 50,20,10 e 1'''

print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédulas de R${céd:.2f}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre!')