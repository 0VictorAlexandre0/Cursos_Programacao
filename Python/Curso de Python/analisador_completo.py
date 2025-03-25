#'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# -a média de idade do grupo
# -o nome do homem mais velho do grupo
# -quantas mulheres tem menos de 20 anos.'''

somaidade = 0
maioridadehomem = 0
nomevelho = 0
totalmulher20 = 0

for i in range(1, 5):
    print('----- {}º PESSOA -----'.format(i))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    somaidade += idade

    if i == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho= nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        totalmulher20 += 1

media = somaidade / 4

print('A média de idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalmulher20))
