# 1- Clicar no menu iniciar
# 2- Pesquisar o bloco de notas
# 3- Pressionar a tecla enter
# 4- Digitar um texto no bloco de notas
# 5- Salvar
# 6- Fechar o bloco de notas

'''
import pyautogui
import time

#configurando pausa entre comandos
pyautogui.PAUSE = 1

#inicio do comando
pyautogui.press("Win")
pyautogui.write("Bloco de Notas", interval= 0.1)
pyautogui.press("Enter")
pyautogui.write("Automação com Python usando PyAutoGUI")
pyautogui.hotkey("ctrl", "s") #tecla de atalho
pyautogui.write("Meu_Primeiro_Arquivo")
pyautogui.press("Enter")
pyautogui.hotkey("alt", "f4")

print("Automação concluída com sucesso!")
'''

'''
Automação para abrir o Bloco de Notas, garantir que uma nova aba
seja aberta antes de começar a digitar e evitar sobrescrita.
'''

import pyautogui
import time
import os
from datetime import datetime

# Define uma pausa de 2 segundos entre os comandos para evitar problemas de execução rápida
pyautogui.PAUSE = 2

# Fecha qualquer instância do Bloco de Notas aberta antes de iniciar
os.system("taskkill /f /im notepad.exe")

# Aguarde um pouco para garantir que foi fechado
time.sleep(2)

#Abrir o menu iniciar do windows
pyautogui.press("win")

#Pesquisar digitando "Bloco de Notas" e pressiona a tecla enter
pyautogui.write("Bloco de Notas", interval=0.1)
pyautogui.press("enter")

#Aguardar abrir o bloco de notas
time.sleep(2)

# Aguardar abrir o Bloco de Notas
time.sleep(2)

# Abrir uma nova aba do Bloco de Notas usando Ctrl + N
pyautogui.hotkey("ctrl", "n")

# Aguardar um pouco para garantir que a nova aba abriu corretamente
time.sleep(1)

# Começar a digitar no Bloco de Notas
pyautogui.write("Texto gerado com Python usando o PyAutoGUI!", interval=0.1)

# Abrir a caixa de diálogo "Salvar Como" usando F12
pyautogui.hotkey("ctrl","shift","s")
#pyautogui.hotkey("f12")

# Aguardar a abertura da caixa de diálogo "Salvar Como"
time.sleep(1)

# Gerar um nome de arquivo dinâmico com base no timestamp
nome_arquivo = datetime.now().strftime("meu_arquivo_%Y%m%d_%H%M%S.txt")
pyautogui.write(nome_arquivo)

# Pressionar Enter para salvar
pyautogui.press("enter")

# Aguarde um pouco para garantir que o arquivo foi salvo
time.sleep(2)

# Fechar o Bloco de Notas corretamente
pyautogui.hotkey("alt", "f4")

# Garantir que o processo foi encerrado corretamente
time.sleep(1)
os.system("taskkill /f /im notepad.exe")

print(f"Automação concluída com sucesso! Arquivo salvo como: {nome_arquivo}")





