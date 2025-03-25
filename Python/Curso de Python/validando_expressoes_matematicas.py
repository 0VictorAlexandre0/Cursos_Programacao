#'''Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu programa deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem certa'''

expressao = input('Digite a expressão: ')
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0: #se a lista não estiver vazia.
            lista.pop() #remover ultimo elemento
        else: #se a lista estiver vazia
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')