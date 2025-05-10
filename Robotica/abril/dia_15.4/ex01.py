#Navegar entre varias paginas e coletar titulos dos livros

import requests
from bs4 import BeautifulSoup

url_site = 'https://books.toscrape.com/catalogue/page-{}.html'

#visitar 3 primeiras paginas
for pagina in range(1,4):
    url = url_site.format(pagina)
    print(f'\nPágina {pagina} - {url}')

    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, 'html.parser')


    livros = soup.find_all('h3')
    for livro in livros:
        titulo = livro.find('a')['title']
        print('Título:', titulo)