#'''Calcule salário, superior a 1250 aumenta 10%,
#para igual ou inferior, 15%.'''

salario = float(input('Qual seu salário? R$'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print('Aumento de 10%, novo valor: R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('Aumento de 15%, novo valor: R${:.2f}'.format(aumento))

