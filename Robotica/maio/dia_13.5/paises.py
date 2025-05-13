import requests

pais = 'Brazil'
url = f'https://restcountries.com/v3.1/name/{pais}'

resposta = requests.get(url)
dados = resposta.json()

#exibir apenas algumas infos

info = dados[0]
print(f'Nome: {info['name']['common']}')
print(f'Capital: {info['capital'][0]}')
print(f'Regiao: {info['region']}')
print(f'Populacao: {info['population']}')















