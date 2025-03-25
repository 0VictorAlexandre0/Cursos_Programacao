#'''Crie um programa que leia duas notas de um aluno e calcule sua
# média, mostrando uma mensagem no final, de acordo com a média
# atingida:
# - media abaixo de 5.0: reprovado
# - media entre 5.0 e 6.9: recuperação
# - media 7.0 ou superior: aprovado'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Você foi reprovado. Média {}'.format(media))
elif 7 > media >=5: #menor que 7 e menor ou igual a 5
    print('Você ficou de recuperação. Média {}'.format(media))
elif media >=7:
    print('Você foi aprovado. Média {}'.format(media))
