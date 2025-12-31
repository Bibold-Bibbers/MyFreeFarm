import pyautogui
import time
import random
import numpy as np

# Falls du Type-Hinting nutzen willst (optional):
# from Location import Location 

class MouseMovement:
    def __init__(self):
        self.sqrt3 = np.sqrt(3)
        self.sqrt5 = np.sqrt(5)

    def moveToLocation(self, location):
        # KORREKTUR: Methode direkt auf der Instanz 'location' aufrufen
        x, y = location.getRandomXAndY() 
        self.moveTo(x, y)

    def moveTo(self, dest_x, dest_y, G_0=9, W_0=3, M_0=15, D_0=12):
        """
        Bewegt die Maus mit dem WindMouse-Algorithmus zum Ziel.
        """
        start_x, start_y = pyautogui.position()
        current_x, current_y = start_x, start_y
        
        v_x = v_y = W_x = W_y = 0

        while (dist := np.hypot(dest_x - start_x, dest_y - start_y)) >= 1:
            W_mag = min(W_0, dist)
            
            if dist >= D_0:
                W_x = W_x / self.sqrt3 + (2 * np.random.random() - 1) * W_mag / self.sqrt5
                W_y = W_y / self.sqrt3 + (2 * np.random.random() - 1) * W_mag / self.sqrt5
            else:
                W_x /= self.sqrt3
                W_y /= self.sqrt3
                if M_0 < 3:
                    M_0 = np.random.random() * 3 + 3
                else:
                    M_0 /= self.sqrt5

            v_x += W_x + G_0 * (dest_x - start_x) / dist
            v_y += W_y + G_0 * (dest_y - start_y) / dist
            v_mag = np.hypot(v_x, v_y)

            if v_mag > M_0:
                v_clip = M_0 / 2 + np.random.random() * M_0 / 2
                v_x = (v_x / v_mag) * v_clip
                v_y = (v_y / v_mag) * v_clip

            start_x += v_x
            start_y += v_y
            
            move_x = int(np.round(start_x))
            move_y = int(np.round(start_y))

            if current_x != move_x or current_y != move_y:
                current_x, current_y = move_x, move_y
                pyautogui.moveTo(current_x, current_y, _pause=False)
                time.sleep(0.001) 

    def leftClick(self):
        pyautogui.leftClick()

    def write(self, text: str):
        pyautogui.write(text, interval=0.1)

    def moveToAndLeftClick(self, x, y):
        self.moveTo(x, y)
        time.sleep(random.gauss(0.1, 0.04))
        self.leftClick()