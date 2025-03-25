#'''Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e menor peso.'''

maiorP = 0
menorP = 0
for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))

    if i == 1: #pega de referencia a primeira ocorrencia/valor
        maiorP = i #logo, o maior e menor serão a mesma coisa
        menorP = i
    else:  #aqui para o resto dos casos do loop
        if peso > maiorP: #o número que acabou de ler (2º) se compara com o valor já obtido (1º) e se alterando se necessario.
            maiorP = peso
        if peso < menorP:
            menorP = peso
print('O maior peso lido foi de {}Kg'.format(maiorP))
print('O menor peso lido foi de {}Kg'.format(menorP))
