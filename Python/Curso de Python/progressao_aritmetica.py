#'''Desenvolva um programa que leia o primeiro termo de uma
# PA. No final, mostre os 10 primeiros termos dessa progressão'''

print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

primeiro_termo = int(input('Primeiro termo: ')) #número que vai iniciar
razao = int(input('Razão: ')) #contagem de tanto em tanto (2 em 2, 3 em 3)
decimo_termo = primeiro_termo + (11 - 1) * razao #mostrar os 10 primeiros termos da razao

for i in range(primeiro_termo, decimo_termo, razao):
    print('{}'.format(i), end=' -> ')
print('Fim')
