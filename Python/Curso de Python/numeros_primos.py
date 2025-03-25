n = int(input('Digite um número: '))
total = 0

for item in range(1, n + 1): #para todos item entre 1 e N
    if n % item == 0: #quando for primo
        print('\033[34m', end='') #código de cor
        total +=1
    else: #quando não for primo
        print('\033[31m', end='') #código de cor
    print('{} '.format(item), end='')
print('\n\033[mO número {} é divisível {} vezes.'.format(n, total))
#pra cor voltar ao normal

if total == 2:
    print('{} é primo.'.format(n))
else:
    print('{} não é primo'.format(n))