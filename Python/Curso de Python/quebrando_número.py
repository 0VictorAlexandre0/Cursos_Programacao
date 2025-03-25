#crie um programa que leia um número real e mostre sua porção inteira

import math  #importar biblioteca math como todas as contas matematicas
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
#trunc/truncade serve para cortar a parte inteira do número

#outra foram de fazer:

from math import trunc  #importei apenas o TRUNC da biblioteca matematica inteira
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#outra forma de fazer sem importar nada
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))