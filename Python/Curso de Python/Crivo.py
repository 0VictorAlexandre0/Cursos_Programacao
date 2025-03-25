limite = int(input('Digite um número: '))
def crivo(limite):
    primos = [True] * (limite + 1)
    primos[0], primos[1] = False, False

    cont = 2
    while cont * cont <= limite:
        if primos[cont]:
            div = cont * cont
            while div <= limite:
                primos[div] = False
                div += cont
        cont += 1

    lista_primos = []
    cont = 2
    while True:
        if primos[cont]:
            lista_primos += [cont]
        cont += 1
        if cont > limite:
            break
    return lista_primos
print(crivo(limite))
