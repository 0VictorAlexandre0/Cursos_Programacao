#""" Crie um programa que leia o nome de uma pessoa
# e diga se ela tem 'SILVA' no nome. """

nome = input('Qual seu nome completo? ').strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
# """a pergunta sendo feita com o 'IN' é: 'Existe silva em nome?' e como é
# '.lower' tem que ser tudo em minusculo na programação, mesma coisa com '.upper'. """