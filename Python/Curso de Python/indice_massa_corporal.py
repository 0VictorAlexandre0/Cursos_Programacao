#'''Calcule o IMC(indice de massa corporea) e mostre seus status:
# abaixo de 18,5: abaixo do peso
# entre 18,5 e 25: peso ideal
# 25 à 30: sobrepeso
# 30 à 40: obdesidade
# 40+: morbida'''

peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2) #peso dividido pela altura ao quadrado
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 18.5 and imc < 25:
    print('Peso ideal')
elif imc <= 25 and imc < 30:
    print('Sobrepeso')
elif imc <= 30 and imc < 40:
    print('Obeso')
else:
    print('Obesidade mórbida')
