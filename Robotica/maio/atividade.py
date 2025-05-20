import requests
from deep_translator import GoogleTranslator


tradutor = GoogleTranslator(source='pt', target='en')

pais_pt = []
for paises in range(3):
    pais = input(f"Digite o {paises+1}º país: ")
    pais_pt.append(pais)

print(f"Países digitados: {pais_pt}")



pais_en = []
for paises in pais_pt:
    pais_traduzido = tradutor.translate(paises)
    print(f"Traduzido para inglês: {pais_traduzido}")
    pais_en.append(pais_traduzido)



for pais in pais_en:
    url = f'https://restcountries.com/v3.1/name/{pais}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        info = dados[0]

        nome = info['name'].get('common', 'Desconhecido')
        nome_oficial = dados['name'].get('official', 'Desconhecido')







        print(f'Nome comum: {info['name']['common']}\nNome oficial: {info['name']['official']}')

        print(f'Capital: {info['capital'][0]}')

        print(f'Continente: {info['continents'][0]}')

        print(f'Região: {info['region']} \nSub-região: {info['subregion']}')

        print(f'População: {info['population']}')

        print(f'Área total: {info['area']}km²')

        print(f'População: {info['population']}')

        print(f'Moeda principal, Simbolo: {info['currencies']['BRL']['symbol']}\nMoeda principal, Nome: {info['currencies']['BRL']['name']}')

        print(f'Idioma principal: {info['languages']['por']}')


        fuso = info.get('timezones', ['sem fuso'])
        for hora in dados:
            print(fuso)


        print(f'Fusos Horários: {info['timezones']}')



    else:
        print("País não encontrado ou erro na requisição.")
