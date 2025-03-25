#veja se a frase é um palindromo, desconsidere espaços.

frase = input('Digite uma frase: ').strip().upper()
#eliminar espaços antes e depois e colocar tudo em maiúsculo

palavras = frase.split() #separar em palavras
junto = ''.join(palavras) #juntar as palavras pelos espaços vazios
inverso = ''

for letra in range(len(junto) -1, -1, -1):
#'''começar em LEN JUNTO -1 para ver o número de letras -1, ou seja frase de 20, tem 19
# ai até a letra 0, ou seja -1 e vai contando de trás pra frente (-1)'''
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')