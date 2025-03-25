# Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique
# o número a calcular e outro chamado show, que será
# um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    Calcular fatorial
    :param num: Número a ser calculado.
    :param show: (opcional) Mostrar o calculo.
    :return: O valor do fatorial num.
    """
    n = 1
    for i in range(num, 0 , -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        n *= i
    return n

help(fatorial)
print(fatorial(5, show=True))
