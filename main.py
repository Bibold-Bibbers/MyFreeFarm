import pyautogui
import pytesseract
import time
from WebsiteLogin import *
from constructionField import *
from Location import Location
from CoordinatesLaptops import XYKoordinatenLabtops



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


"""
ackerLoc = Location(900, 380, 80, 80)
anpflanzenSymbolLoc = Location(960, 375, 40, 30)
waterSymbolLoc = Location(1020,375, 20, 20)
erntenSymbolLoc = Location(1070, 375, 40, 30)
"""

ackerLoc = Location(900, 380, 80, 80)
anpflanzenSymbolLoc = Location(670, 330, 25, 30)
waterSymbolLoc = Location(740,335, 25, 30)
erntenSymbolLoc = Location(820, 335, 40, 30)

#LinuxCoordinates = XYKoordinatenLabtops(xStart=850, xEnd=1330, yStart=470, yEnd=870)

MacCoordinates = XYKoordinatenLabtops(isMac=True,
                                      xStart=610,
                                      xEnd= 1080,
                                      yStart= 455,
                                      yEnd= 850, 
                                      yLoginStart=180,
                                    yLoginPWStart=180, 
                                    xLoginButton=1000, 
                                    loginHeight=20, 
                                    loginWidth=100, 
                                    xLoginPWStart=800, 
                                    xLoginStart=630, 
                                    xBrowserSearch=750, 
                                    yBroserSearch=65, 
                                    yLoginButton=180)






ackerEins = Acker(ackerLoc, erntenSymbolLoc, anpflanzenSymbolLoc, waterSymbolLoc, MacCoordinates)
time.sleep(2)
ackerEins.checkEverySingleFieldForWeeds()
time.sleep(2)

###Plant auswählen funktioniert noch nicht, aber ernten schon gut. Also die Methode clickonEveryFreeField
ackerEins.harvestPlantWater('sc/strawberry.png')

"""
websiteLogin = WebsiteLogin(MacCoordinates) 
websiteLogin.searchBrowserURL()
websiteLogin.loginFromHomePage()





Acker X 940 Y 411
Anpflanzen X 977 Y 390
Ernten X 1090 Y385

position = pyautogui.locateAllOnScreen(search_bild, confidence=0.5)
print(position)
for i in position:
    pyautogui.moveTo(i.left + 10, i.top + 10, duration=1)
    time.sleep(1)
"""

