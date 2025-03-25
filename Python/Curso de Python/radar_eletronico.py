#'''Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada KM
# acima do limite.'''

velocidade = float(input('Qual a velocidade do carro? (Em Km/h): '))
if velocidade <= 80:
    print('Parabéns, continue dirigindo com segurança.')
else:
    multa = (velocidade-80) * 7
    print('Passou do limite de velocidade de 80km/h, sua multa será de R${:.2f}'.format(multa))


#cod guana

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

