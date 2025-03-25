cores = ('\033[m',          # 0 - sem cor
         '\033[0;30;41m',   # 1 - vermelho
         '\033[0;30;42m',   # 2 - verde
         '\033[0;30;43m',   # 3 - amarelo
         '\033[0;30;44m',   # 4 - azul
         '\033[0;30;45m',   # 5 - roxo
         '\033[0;30;47m')   # 6 - branco (fundo branco, texto preto)



for i, cor in enumerate(cores):
    print(f'{cor}Teste da cor {i}\033[m')