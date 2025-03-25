#Crie um programa que leia o nome e media de um
#aluno, guardando também a situação em um dicionario.
#No final, mostre o conteudo em uma tabela.


aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['media'] < 6:
    aluno['situação'] = 'reprovado'
else:
    aluno['situação'] = 'aprovado'

print('-='*30)

for key, value in aluno.items():
    print(f'{key} é igual a {value}')
