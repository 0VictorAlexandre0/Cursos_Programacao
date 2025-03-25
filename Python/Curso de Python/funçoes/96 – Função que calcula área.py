#Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.


def terreno(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno de {largura} x {comprimento} é de {area:.2f}m2')


print('Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
terreno(l, c)

