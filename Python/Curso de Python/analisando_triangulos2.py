r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo.')
    if r1 == r2 and r2 == r3: #tambem pode ser feito 'r1 == r2 == r3'
        print('Forma um triângulo Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Forma um triângulo Isósceles.')
    elif r1 != r2 and r2 != r3 and r3 != r1: # 'r1 != r2 != r3 != r1'
        print('Forma um triângulo Escaleno.')
else:
    print('Os segmentos não podem formar um triângulo.')
