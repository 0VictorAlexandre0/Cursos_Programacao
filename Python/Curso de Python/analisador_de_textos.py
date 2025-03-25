#"""Crie um programa que leia o nome completo de uma pessoa e mostre:
# -O nome com todas as letras maiusculas e minusculas
# -Quantas letras tem (sem contas espaços)
# -Quantas letras tem o primeiro nome."""

nome = input('Digite seu nome completo: ').strip()
#para remover espaços adicionais no começo e no fim

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# ( - nome.count(' ') é para remover (-) foi usado para remover os espaços (' ') no meio da frase.

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#você encontra o espaço do primeiro nome e contará até ele, ficando assim o primeiro nome.

#outra forma de fazer (que eu tentei pela lógica e não consegui) era:
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#"""criei a variavel 'separa' para o 'split' fazer a divisão das palavras na frase,
# [0] para mostrar a primeira palavra e 'len(separa[0])' para contar as letras da
# primeira palavra do 'separa'."""
