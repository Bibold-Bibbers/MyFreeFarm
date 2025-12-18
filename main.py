import pyautogui
import pytesseract
import time
from newArrayApproach import *
from locationVariable import Location



"""
time.sleep(4)
pyautogui.moveTo(850,460)
time.sleep(2)
pyautogui.moveTo(1335,460)
time.sleep(3)
pyautogui.moveTo(945, 460)
time.sleep(3)
pyautogui.moveTo(1210, 460)


"""

carrot = 'sc/carrot.png'
wheat = 'sc/wheat.png'
anbauPflanze = 'sc/carrotZumAnbauen.png'

ackerLoc = Location(900, 380, 80, 80)
anpflanzenSymbolLoc = Location(960, 375, 40, 30)
waterSymbolLoc = Location(1020,375, 20, 20)
erntenSymbolLoc = Location(1070, 375, 40, 30)



ackerEins = Acker(ackerLoc, erntenSymbolLoc, anpflanzenSymbolLoc, waterSymbolLoc)
time.sleep(5)

ackerEins.testFieldXY()


"""
Acker X 940 Y 411
Anpflanzen X 977 Y 390
Ernten X 1090 Y385

position = pyautogui.locateAllOnScreen(search_bild, confidence=0.5)
print(position)
for i in position:
    pyautogui.moveTo(i.left + 10, i.top + 10, duration=1)
    time.sleep(1)
"""

