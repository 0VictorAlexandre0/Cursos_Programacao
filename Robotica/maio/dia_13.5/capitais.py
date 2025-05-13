import requests

url = f'https://restcountries.com/v3.1/all'

resposta = requests.get(url)
dados = resposta.json()

#Percorrer paises e exibir nome e capitais
for pais in dados:
    nome = pais['name']['common']
    capital = pais.get('capital', ['Sem capital'][0])
    print(f'País: {nome} -> Capital: {capital}')





