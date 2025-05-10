import requests
from bs4 import BeautifulSoup
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


#Funçao para extrair dados de livros da pagina web
def extrair_livros(pagina):
    try:
        url= f'https://books.toscrape.com/catalogue/page-{pagina}.html'
        response = requests.get(url)
        if response.status_code != 200:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        livros = []

        for artigo in soup.find_all('article', class_='product_pod'):
            titulo = artigo.h3.a['title']
            preço = artigo.find('p', class_='price_color').text.strip()
            disponibilidade = artigo.find('p', class_='instock availability').text.strip()
            livros.append({
                'Titulo': titulo,
                'Preço': preço,
                'Disponibilidade': disponibilidade
            })
        return livros
    except Exception as e:
        print(f'Erro ao extrair livros da pagina {pagina}: {e}')
        return []

print(extrair_livros(5))


#Função pra exportar pro excel

#Função para exportar para PDF

#Função pra gerar um menu do usuario

#O codigo para de executar quando o usuario digitar 0

