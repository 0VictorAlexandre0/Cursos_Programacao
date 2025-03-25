def metade(num):
    metade = num // 2
    print(f'A metade de R${num} é R${metade:.1f}')

def dobro(num):
    dobro = num * 2
    print(f'O dobro de R${num} é R${dobro:.1f}')

def aumentar(num):
    aumentar = num + ((num * 10) / 100)
    print(f'Aumentando 10% de R${num} é R${aumentar:.1f}')

def diminuir(num):
    diminuir = num - ((num * 10) / 100)
    print(f'Diminuindo 10% de R${num} é R${diminuir:.1f}')
