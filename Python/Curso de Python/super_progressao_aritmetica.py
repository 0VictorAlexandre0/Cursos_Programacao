print('Gerador de PA')
print('-='*10)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

cont = 1
total = 0
termos = 10

while termos != 0:
    total += termos #total=0, termos=10, 0=0+10=10, se termos for 0 finaliza.

    #aqui já são os 10 primeiros termos mostrados.
    while cont <= total: #aqui total=10 + os novos termos que forem digitados.
        print('{} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('Pausa')
    termos = int(input('Quantos termos você quer mostrar a mais? ')) # se for 0, finaliza
print('Progressão finalizada com {} termos.'.format(total))


