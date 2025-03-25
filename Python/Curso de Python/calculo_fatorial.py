#'''Existe 2 formas de fazer'''

'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

n = int(input('Digite um número para calcular seu fatorial: '))
contador = n
fatorial = 1 #toda multiplicação/divisão limpa, é sempre por 1.
print('Calculando {}!'.format(n))
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    #print X se o contador for menor que 1, senão print =.
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))