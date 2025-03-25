#'''Faça um programa que leia três números e
# mostre qual é o maior e menor números.'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#verificar menor:
menor = a #supondo que o 'a' seja menor:
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#verificar maior:
maior = a #supondo que o 'a' seja maior:
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))

