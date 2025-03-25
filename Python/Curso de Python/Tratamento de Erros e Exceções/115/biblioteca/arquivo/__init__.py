def linha(tamanho = 42):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt= read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt = write text, + pra ele criar se nn existir
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
