#Capturar uma imagem da tela

import pyautogui

screenshot = pyautogui.screenshot()
screenshot.save("imagem_tela.png")
print('Imaagem salva com sucesso!')

