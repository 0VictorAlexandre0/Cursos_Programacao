#'''Crie um programa que tenha uma tupla com várias
# palavras. Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.'''

palavras = ('Python', 'Programador', 'Curso', 'Linguagem', 'Futuro')

for item in palavras:
    print(f'\nNa palavra {item.upper()} temos: ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
