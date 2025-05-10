#Navegação automatica ate acabar as pagina do catalogo

import requests
from bs4 import BeautifulSoup

pagina = 1
encontrou = True

while encontrou:
    url = f'https://books.toscrape.com/catalogue/page-{pagina}.html'
    response = requests.get(url)

    if response.status_code != 200:
        break #pagina inexistente

    soup = BeautifulSoup(response.text, 'html.parser')
    livros = soup.find_all('h3')


    if not livros:
        break

    print(f'\nPágina {pagina}')
    for livro in livros:
        titulo = livro.find('a')['title']
        print(f'Livro: {titulo}')

    pagina += 1




