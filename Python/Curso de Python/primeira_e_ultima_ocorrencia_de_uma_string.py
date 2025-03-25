# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece pela primeira vez e última.

frase = input('Digite uma frase: ').upper().strip()
#transforma toda a frase em maiuscula. Remover espaços
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1)) # +1 para mostrar melhor pro usuário que é a posição 1.
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1)) # procure "A" a apartir do lado direito(procurar o 'A' de trás pra frente).