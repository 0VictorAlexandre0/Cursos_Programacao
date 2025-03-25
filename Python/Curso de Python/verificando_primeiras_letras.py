#""" Crie um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome 'SANTO'. """

cidade = input('Em que cidade você nasceu? ').strip()
print(cidade[:5].upper() == 'SANTO')
#Escreve a cidade começando na letra 0 e indo até 5(número de caracteres em 'SANTO'.
# '.upper' para não importa oque o usuário digitar, será transformado para maiúsculo e será TRUE.
