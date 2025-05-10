from bs4 import BeautifulSoup
" extrair dados de páginas web. Ela permite navegar e buscar facilmente por elementos HTML e XML, como tags, classes, ids, textos etc."

"criar um html dentro do python"
html = '''
    <html>
        <body>
            <h1>Olá Mundo!</h1>
            <p class="mensagem">Bem-vindo ao Web Scraping!</p>
            <p>Opa, bão?</p>
        </body>
    </html>
'''

soup = BeautifulSoup(html, 'html.parser')
"BeautifulSoup te permite fatiar o HTML para pegar só o que você quer — como se estivesse navegando por partes de uma árvore de tags."

print(soup.h1.text) #printar o texto de "h1"
print(soup.find('p').text) #procurar a 1 ocorrencia de "p"

#aqui pega todos os "p" como uma lista, mas prescisa percorrer agr
todos = soup.find_all('p')
print(todos)