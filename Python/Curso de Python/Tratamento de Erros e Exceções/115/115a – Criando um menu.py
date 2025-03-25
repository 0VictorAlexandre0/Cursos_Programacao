#Vamos criar um menu em Python, usando modularização.

from biblioteca.interface import *
from biblioteca.arquivo import *
from time import sleep


arquivo = 'testeArquivo.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro, digite uma opção válida!\033[m')
    sleep(2)
