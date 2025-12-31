import pyautogui
import pytesseract
import time
from WebsiteLogin import *
from constructionField import *
from constructionChicken import *
from constructionCow import *
from Location import Location
from CoordinatesLaptops import XYKoordinatenLabtops



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




time.sleep(2)
mouse = MouseMovement()
chicken = Chicken(15,True,True,mouse)


ret = getAllCoordinatesRGB("sc/constructionBuildings/chickenFarm.png", 70, 70, True, 0.5)
print(ret)
for location in ret:
    x, y = location.getRandomXAndY()
    time.sleep(0.8)
    mouse.moveToAndLeftClick(x,y)
    chicken.feedChicken()
    









