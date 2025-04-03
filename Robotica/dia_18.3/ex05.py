import pyautogui
import time

#definir uma área
area_X1, area_Y1 = 500, 300 #canto superior esquerdo
area_X2, area_Y2 = 600, 400 #canto inferior direito

print("Mova o cursor para exibir sua posição")

while True:
    x, y = pyautogui.position() #capturar posição do mouse

    #verificar se o cursor está no local certo
    if area_X1 <= x <= area_X2 and area_Y1 <= y <= area_Y2:
        pyautogui.click(x, y) #simular click do cursor
        print(f"Click automático em: X={x}, Y={y}")
        time.sleep(2)
    else:
        print(f"Cursor fora da área: X={x}, Y={y}")
    time.sleep(1)
