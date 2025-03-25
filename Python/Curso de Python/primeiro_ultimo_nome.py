#""" Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente."""

nome = input('Digite seu nome completo: ').strip()
x = nome.split() #vai pegar o nome e fatiar ele em partes.
print('Seu primeiro nome é {}'.format(x[0])) # 0 por ser o primeiro nome.
print('Seu último nome é {}'.format(x[len(x)-1])) #contar todas as posiçao de nome e -1 para parar nele.

