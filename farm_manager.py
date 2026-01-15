from getCoordinates import *
import time
from constructionChicken import *
from constructionCow import *

class FarmManager:
    def __init__(self, farmManager = None, isMac : bool = True):
        if (farmManager == None):
            self.mouseMovement = MouseMovement()
            self.chickens = []
            self.isMac = isMac
        else:
            self.farmManager = farmManager

    def getAllFields(self):
        self.getChickenFields()
        self.getCowFields()

    def getChickenFields(self):
        ret = getAllCoordinatesRGB("sc/constructionBuildings/chickenFarm.png", 70, 70, True, 0.5)
        chicken = Chicken(10,True, self.isMac,self.mouseMovement)

        for location in ret:
            x, y = location.getRandomXAndY()
            time.sleep(0.8)
            self.mouseMovement.moveToAndLeftClick(x,y)
            time.sleep(0.1)
            chicken.feedChicken()
    
    def getCowFields(self):
        ret = getAllCoordinatesRGB("sc/constructionBuildings/cowFarm.png", 70, 70, True, 0.5)
        cow = Cow(10,True, self.isMac,self.mouseMovement)

        for location in ret:
            x, y = location.getRandomXAndY()
            time.sleep(0.8)
            self.mouseMovement.moveToAndLeftClick(x,y)
            time.sleep(0.12)
            cow.feedCows()