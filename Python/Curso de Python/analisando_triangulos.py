#'''Desenvolva um programa que leia o comprimento de
# três retas e diga se elas podem ou não formar um triângulo'''

#'''regra matemática: cada um dos seguimentos tem que ser menor
# do que a soma do comprimento dos outros dois'''

segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Os segmentos podem formar um triângulo.')
else:
    print('Os segmentos não podem formar um triângulo.')