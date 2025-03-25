#'''Crie um programa que leia nome e duas notas de vários
# alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.'''

ficha = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media]) #posição 0, 1, 2
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
    print('-='*30)
print('-='*30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for item, lista in enumerate(ficha):
    print(f'{item:<4} {lista[0]:<10} {lista[2]:>8}') #lita[0] e lista[2] é a posição
print('-'*25)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas <= len(ficha) - 1:
        print(f'Notas de {ficha[notas][0]} são {ficha[notas][1]}')
        print('-'*25)
    if notas == 999:
        print('Finalizando...')
        break
print('Volte sempre!')
