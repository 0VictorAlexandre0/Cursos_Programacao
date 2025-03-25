#'''Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é
# a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando a flag).'''

#meu código fiz sozinho
soma = 0
n = 0
cont = 0
#ou (soma = n = cont = 0), todos são iguais a 0.

while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        cont += 0
    else:
        cont += 1
        soma += n
print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))