print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)

cont = homem = mulher = 0

while True:
    idade = int(input('Idade: '))
    if idade > 18:
        cont += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
        if sexo == 'M':
            homem += 1
        if idade < 20 and sexo == 'F':
            mulher += 1
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
    print('-' * 30)

print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos')
