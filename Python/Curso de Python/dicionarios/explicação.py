#Variáveis compostas

#Dicionarios são parecidos com tuplas e listas,
#porem com indices personalizaveis

#dicionarios = { }
# dados = {'nome': 'Pedro', 'idade': 25}

#não é possivel usar o 'append' em dicionarios
#para add novo elemento é:
    # dados['sexo'] = 'M'
    # dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}

#para remover elementos:
    #del dados['idade']
    # dados = {'nome': 'Pedro', 'sexo': 'M'}

#exp:
    #filme = {'titulo: 'Star Wars',
    #         'ano': 1977,
    #         'diretor': 'George Lucas'
    #        }
    # print(filme.values()) printa elementos
    # print(filme.keys()) printa os indices
    # print(filme.items()) printa TUDO

    # for K, V in filme.items():
    #   print(f'O {K} é {V}

    # O titulo é Star Wars
    # O ano é 1977
    # O diretor é George Lucas

#É possível utilizar listas, tuplas e dicionarios todos juntos,
#voce pode criar uma lista 'Locadora' e colocar tuplas de filmes la dentro

#print(locadora[0]['ano'])
#1977

#Nao é possivel usar fatiamento em tuplas, para fazer a copia
#dela e colocar outro elemento durante um input por exemplo,
#se usa o metodo 'copy()', lista.append(tupla.copy())