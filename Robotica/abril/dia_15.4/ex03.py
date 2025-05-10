#Navegar e extrair os links e titulos

import requests
from bs4 import BeautifulSoup

url_site = 'https://books.toscrape.com/catalogue/page-{}.html'
detalhes_url = 'https://books.toscrape.com/catalogue/'

for pagina in range(1,6):
    url = url_site.format(pagina)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f'\nPágina {pagina}')


    livros = soup.find_all('h3')
    for livro in livros:
        link = livro.find('a')['href']
        titulo = livro.find('a')['title']


    	#ajuste do link de detalhes
        detalhes = detalhes_url + link
        print(f'{titulo} --> {detalhes}')



