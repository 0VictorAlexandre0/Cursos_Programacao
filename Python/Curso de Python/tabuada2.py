num = int(input('Digite um número para fazer sua tabuada: '))
for n in range(1, 11):
    print('{} x {} = {}'.format(num, n, num*n))
    #vai escrever o numero vezes 1 a 10 e depois o resultado