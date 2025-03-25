#'''Desenvolva um programa que leia quatro valores pelo teclado
# e guarde - os em uma tupla. No final, mostre:
# - Quantas vezes apareceu o valor 9
# - Em que posição foi digitado o primeiro valor 3
# - Quais foram os números pares.'''


n = (int(input('Digite o primeiro valor: ')),
     int(input('Digite o segundo valor: ')),
     int(input('Digite o terceiro valor: ')),
     int(input('Digite o quarto valor: ')))

print(f'\nVocê digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
     print(f'O valor 3 apareceu {n.index(3)+1}ª posição.')
else:
     print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for i in n:
     if i % 2 == 0:
          print(i, end=' ')
