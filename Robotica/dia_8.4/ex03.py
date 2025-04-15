import requests
from bs4 import BeautifulSoup

'''
buscar noticias em sites simples
https://g1.globo.com
'''

url = 'https://g1.globo.com'
resposta = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resposta.text, 'html.parser')

for manchete in soup.find_all('a', class_='feed-post-link'):
    print(manchete.text.strip())
    print()









