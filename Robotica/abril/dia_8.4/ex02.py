#Trazer todo conteúdo de um site
import requests
'''
    url = 'https://google.com'
    resposta = requests.get(url)

    print(resposta.text) #traz o codigo fonte do google
'''


#Fazer requisição API rest
'''
    url = 'https://api.agify.io/?name=Victor'
    resposta = requests.get(url)

    dados = resposta.json()
    print(dados)
'''


#Envio de dados via POST
'''
    url = 'https://httpbin.org/post'
    dados = {'nome': 'Victor', 'idade': 19}
    resposta = requests.post(url, data=dados)

    print(resposta.json())
'''


#Verificar status da pagina Web
url = 'https://google.com'
resposta = requests.get(url)

if resposta.status_code == 200:
    print("ta on")
else:
    print('ta off')










