import math
import random
import pyautogui
from constructionField import Acker
from CoordinatesLaptops import XYKoordinatenLabtops
from mouseMovement import *
import time
import pyperclip

class WebsiteLogin:
    def __init__(self, XYKoordinatenLaptop : XYKoordinatenLabtops):
        self.mouseMovement = MouseMovement()
        self.searchBrowserX = XYKoordinatenLaptop.getXBroswerSearch()
        self.searchBrowserY = XYKoordinatenLaptop.getYBrowserSearch()
        self.computerKoorinates = XYKoordinatenLaptop
        self.isMac = XYKoordinatenLaptop.getIsMac()

    def searchBrowserURL(self):
        url = "https://www.myfreefarm.de"
        pyautogui.moveTo(self.searchBrowserX,self.searchBrowserY,0.5)
        pyautogui.leftClick(duration=0.2)
        self.copyPaste(url)
        
        time.sleep(0.4)
        pyautogui.press('enter', interval=0.1)
        time.sleep(0.4)

    def loginFromHomePage(self):
        email = "yobegag893@discounp.com"

        x,y = self.computerKoorinates.getLoginRandominizedXY()
        self.mouseMovement.moveTo(x,y)
        self.mouseMovement.leftClick()
        time.sleep(random.gauss(0.4,0.15))
        self.copyPaste(email)

        time.sleep(random.gauss(0.3,0.1))
        x,y = self.computerKoorinates.getLoginPWRandominizedXY()
        self.mouseMovement.moveTo(x,y)
        self.mouseMovement.leftClick()
        password = "XTRXY7WR7@4PA)i"
        self.copyPaste(password)
        time.sleep(random.gauss(0.34,0.18))

        x,y = self.computerKoorinates.getLoginButtonRandomizedXY()
        self.mouseMovement.moveTo(x,y)
        self.mouseMovement.leftClick()

    def copyPaste(self, text):
        pyperclip.copy(text)
        time.sleep(0.05)
        if self.isMac:
            pyautogui.hotkey('command', 'v')
        else:
            pyautogui.hotkey('ctrl', 'v')
