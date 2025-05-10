#Descobrindo posição do mouse:

import pyautogui
import time

print('Mova o mouse para descobrir a posição do cursor')
try:
    while True:
        x, y = pyautogui.position()
        print(f'Posição atual X={x}, Y={y}', end='\r')
        #time.sleep(0.5)
except KeyboardInterrupt:
    print('\nCaptura interrompida!')




