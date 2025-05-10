import pyautogui

senha = pyautogui.password("Informe sua senha:")
#print(senha) mostrar senha

if senha == "admin":
    pyautogui.alert("Acesso liberado!")
else:
    pyautogui.alert("Acesso negado!")