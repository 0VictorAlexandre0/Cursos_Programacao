import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) #raiz normal/real

#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
#ceil é arredondamento para cima

#print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
#floor é arredondamento para baixo

from math import sqrt, floor   #esse aqui eu só chamei a sqrt/raiz quadrada e arredondamento
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))