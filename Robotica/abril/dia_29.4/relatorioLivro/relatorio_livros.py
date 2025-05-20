import requests
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl.styles import Font

#Função para extrair as infos da pagina web
def extrair(url_base, url_pagina):
    resposta = requests.get(url_base + url_pagina)
    soup = BeautifulSoup(resposta.text, 'html.parser')

    livros = soup.find_all('article', class_='product_pod')

    dados = []
    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='price_color').text
        disponibilidade = livro.find('p', class_='instock availability').text
        link = url_base + livro.h3.a['href']

        dados.append({
            'Título': titulo,
            'Preco' : preco,
            'Disponibilidade' : disponibilidade,
            'Link' : link
        })

    return dados

#1- URL base
url_base = 'https://books.toscrape.com/'
todos_livros = []

for pagina in range(1,4):
    if pagina == 1:
        url_pagina = 'index.html'
    else:
        url_pagina = f'catalogue/page-{pagina}.hmtl'
    
    livros_pagina = extrair(url_base, url_pagina)
    todos_livros.extend(livros_pagina)


#3- criar dataframe
df = pd.DataFrame(todos_livros)


#4- Salvar Excel
df.to_excel('relatorio_livros.xlsx', index=False, engine='openpyxl')

print('Arquivo craido!')


