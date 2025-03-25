n = int(input("Digite um número positivo: "))

while n < 0 or n > 10:
    print("Por favor, digite um número positivo entre 0 e 10.")
    n = int(input("Digite um número positivo: "))

print('{} x {} = {}'.format(n, 1, n*1))
print('{} x {} = {}'.format(n, 2, n*2))
print('{} x {} = {}'.format(n, 3, n*3))
print('{} x {} = {}'.format(n, 4, n*4))
print('{} x {} = {}'.format(n, 5, n*5))
print('{} x {} = {}'.format(n, 6, n*6))
print('{} x {} = {}'.format(n, 7, n*7))
print('{} x {} = {}'.format(n, 8, n*8))
print('{} x {} = {}'.format(n, 9, n*9))
print('{} x {} = {}'.format(n, 10, n*10))