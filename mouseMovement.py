from locationVariable import *
import pyautogui

class MouseMovement:
    def __init__(self):
        pass

    def moveToLocation(self, location : Location):
        x,y = Location.getRandomXAndY(location)
        self.moveTo(x,y)

    ##Maybe add switch Cases. So if I go through a field it should be quicker and randomly stop. So add a int with each number represents something
    def moveTo(self, x, y):
        pyautogui.moveTo(x,y, duration=0.5)
        
    def leftClick(self):
        pyautogui.leftClick()

    def write(self, text : str):
        pyautogui.write(text, interval=0.1)