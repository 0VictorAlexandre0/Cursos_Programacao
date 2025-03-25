distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
    print('A passagem fica por RS{:.2f}'.format(preço))
else:
    preço = distancia * 0.45
    print('A passagem com desconto fica por R${:.2f}'.format(preço))
