def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * taxa / 100)
    if formato == False:
        return res
    else:
        return moeda(res)

def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * taxa / 100)
    return res if formato == False else moeda(res)

def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato == False else moeda(res)

def metade(preco = 0, formato = False):
    res = preco / 2
    return res if formato == False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco = 0, taxaAume = 10, taxaDimi = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaAume}% de aumento: {aumentar(preco, taxaAume, True)}')
    print(f'Com {taxaDimi}% de redução: {diminuir(preco, taxaDimi, True)}')
    print('-' * 30)
