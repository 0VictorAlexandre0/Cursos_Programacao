import os
import pyautogui

def verificaArquivo(nomeArquivo):
    if os.path.exists(nomeArquivo):
        pyautogui.alert("Arquivo encontrado!")
    else:
        pyautogui.alert("Arquivo não encontrado!")


def verificaUsuario(senha):
    if senha == "admin":
        verificaArquivo("dados.csv")
        local = "C:/Users/legob\OneDrive/Área de Trabalho"
        listarArquivos(local)
    else:
        pyautogui.alert("Senha inválida! Finalizando processo...")


#ela fará uma lista de arquivos que há em determinado diretorio
def listarArquivos(diretorio):
    for arquivo in os.listdir(diretorio):
        print(f"Processando: {arquivo}")
    print("Processo finalizado!")


usuario = pyautogui.password("Informe a senha:")
verificaUsuario(usuario)

