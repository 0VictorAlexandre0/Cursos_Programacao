#'''Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.'''

continuar = 'S'
soma = quantidade = 0

while continuar in 'Ss': #enquanto estiver em
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1

    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = input('Quer continuar? [S/N] ').upper().strip()
media = soma / quantidade

print('Você digitou {} números e a média foi {:.2f}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
