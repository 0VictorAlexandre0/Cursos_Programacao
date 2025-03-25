#'''Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para valor cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for
# negativo.'''

while True:
    n = int(input('\nQuer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for i in range(1, 11):
        resp = n * i
        print(f'{n} x {i} = {resp}')
print('-' * 30)
print('Programa encerrado. Volte sempre!')
