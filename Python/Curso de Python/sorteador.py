import random

#modulo de randomizador de elementos

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Querto aluno: ')

lista = [nome1, nome2, nome3, nome4] #lista fica dentro de colchetes
escolhido = random.choice(lista) #uma escolha dentro da lista

print('O aluno escolhido foi {}'.format(escolhido))
