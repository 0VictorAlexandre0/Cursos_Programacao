#'''Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1- binario
# 2- octal
# 3- hexadecimal'''

numero = int(input('Digite qualquer número inteiro: '))
print('''Escolha uma das bases para a conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:])) #'bin' conversor para binario
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:])) #'oct' conversor para octal
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:])) #'hex' conversor para hexadecimal
else:
    print('Opção invalida. Tente novamente.')

#'''os resultados estão dando "0b...", "0o..." e "0x..."
# para tirar esses sinalizadores, use a técnica de
# 'Fatiamento de Strings' [2:] '''