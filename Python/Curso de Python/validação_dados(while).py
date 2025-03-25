#'''Faça um programa que leia o sexo de uma pessoa, mas só
# aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.'''

sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
#sem espaços, maiúsculo e 1º letra apenas.
while sexo not in 'MmFf': #enquanto {} não estiver em {}...
    sexo = input('Dados inválidos. Por favor digite novamente: ').strip().upper()[0]
print('Dados registrados com sucesso!')
