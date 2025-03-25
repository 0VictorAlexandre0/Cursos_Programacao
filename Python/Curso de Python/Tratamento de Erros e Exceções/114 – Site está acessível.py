#Crie um código em Python que teste se o site
# pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pokemon.com')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site.')
