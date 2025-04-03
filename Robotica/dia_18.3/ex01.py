import os #pra tabalhar com o sistema operacional
import pyautogui

arquivo = "dados.csv"

#O path é usado para manipular caminhos de arquivos e diretórios
if os.path.exists(arquivo):
    #verificar se o arquivo existe
    pyautogui.alert("Arquivo encontrado!")
else:
    pyautogui.alert("Aquivo não encontrado!")