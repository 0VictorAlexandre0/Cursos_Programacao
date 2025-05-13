#1- Importação das bibliotecas
import requests
import sqlite3


#2- Coletar dados de uma API
pais = 'Greece'
url = f'https://restcountries.com/v3.1/name/{pais}'
resposta = requests.get(url)
dados = resposta.json()

info = dados[0]
nome = info['name']['common']
capital = info['capital'][0] if 'capital' in info else 'N/A'
#se capital existir em info ele aparece, se não, não existe
regiao = info['region']
populacao = info['population']

print('Dados extraidos da API')
print(f'Nome: {nome}')
print(f'Capital: {capital}')
print(f'Região: {regiao}')
print(f'População: {populacao}')


#3- Criar e conectar BD
conexao = sqlite3.connect('paises.db')
cursor = conexao.cursor()

#3.1- Criação de uma tabela se ela não existir
cursor.execute('''
               CREATE TABLE IF NOT EXISTS paises(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    capital TEXT,
                    regiao TEXT,
                    populacao INTEGER
                )
               ''')

#4 - Inserir as informações Coletadas
cursor.execute('''
                INSERT INTO paises(nome, capital, regiao, populacao)
                VALUES(?,?,?,?)
                ''',(nome, capital, regiao, populacao))
conexao.commit()


#5- Consultar as informações inseridas
print('\nDados inseridos no Banco:')
cursor.execute('SELECT * FROM paises')
for linha in cursor.fetchall():
    print(linha)


#6- Fechar conexão
conexao.close()






