#'''Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.'''

soma = 0 #var acumuladora
cont = 0 #var contadora

for inter in range(1, 501, 2):
#agora so vai mostrar todos os numeros pulando de 2 em 2 pq nn sao multiplos de 3
    if inter % 3 == 0:
        cont = cont + 1
        soma = soma + inter #var acumuladora
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))


#'''para resolver o exerc, é preciso usar o conceito de
# var acumuladora e contadora'''