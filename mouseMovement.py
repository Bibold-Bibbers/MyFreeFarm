from locationVariable import *
import pyautogui

class MouseMovement:
    def __init__(self):
        pass

    def moveToLocation(self, location : Location):
        x,y = Location.getRandomXAndY(location)
        self.moveTo(x,y)

    def moveTo(self, x, y):
        pyautogui.moveTo(x,y, duration=0.5)
        
    def leftClick(self):
        pyautogui.leftClick()