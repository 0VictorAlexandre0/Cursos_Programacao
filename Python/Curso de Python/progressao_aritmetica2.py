print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1

while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao #primeiro=2, razao=3, 2=2+3=5 2+=3=5
    cont += 1
print('Fim')
