#""" Faça um programa que leia de 0 a 9999 e mostre na tela
# cada um dos digitos separados: unidade, centena, dezena e milhar."""

#num = int(input('Informe um número: '))
#n = str(num) #converti o int em str
#print('Analise o número {}'.format(num))
#print('Unidade {}'.format())
#print('Dezena {}'.format())
#print('Centena {}'.format())
#print('Milhar {}'.format())

# 1234
# unidade(4) = 3
# dezena(3) = 2
# centena(2) = 1
# milhar(1) = 0

#esse código só funciona se o usuário digitar 4 números, por isso ele nao é eficaz

# o "certo" seria:
num = int(input('Informe um número: '))

unidade = num // 1 % 10 # // é divisão inteira e % é o resto da divisao(módulo)
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Análise do número {}'.format(num))
print('Unidade {}'.format(unidade))
print('Dezena {}'.format(dezena))
print('Centena {}'.format(centena))
print('Milhar {}'.format(milhar))