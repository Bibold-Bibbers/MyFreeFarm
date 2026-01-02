import pyautogui
import pytesseract
import time
import json
from WebsiteLogin import *
from constructionField import *
from constructionChicken import *
from constructionCow import *
from Location import Location
from CoordinatesLaptops import XYKoordinatenLabtops
from farmManager import FarmManager
from RemoveAds import *



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


websiteLogin = WebsiteLogin(MacCoordinates)
mouseMovement = MouseMovement()
farmManager = FarmManager()
websiteLogin.searchBrowserURL()
time.sleep(4)
# 1. Datei öffnen und laden
with open('config/accounts.json', 'r') as file:
    users = json.load(file)

for user in users:
    email = user['email'] 
    passwort = user['password']
    websiteLogin.loginFromHomePage(email, passwort)
    time.sleep(3)
    checkForAdds(MacCoordinates.getIsMac(), mouseMovement)
    farmManager.getAllFields()
    time.sleep(1)
    websiteLogin.logOut()
    time.sleep(2)




#time.sleep(2)
#farmManager = FarmManager()
#farmManager.getAllFields()
    









