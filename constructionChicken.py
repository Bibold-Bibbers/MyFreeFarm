from getCoordinates import *
from mouseMovement import MouseMovement
import time
import random

class Chicken:
    def __init__(self, chickenCount, onlyOneFoodSupply : bool, isMac :bool, mouseMovement : MouseMovement):
        self.chickenCount = chickenCount
        self.onlyOneFoodSupply = onlyOneFoodSupply
        self.isMac = isMac
        self.mouseMovement = mouseMovement

    def feedChicken(self):
        time.sleep(0.1)
        self.acceptProductsIfThere()
        time.sleep(0.1)

        locationWheat = getCoordinatesRGB("sc/chicken/wheatForChicken.png", 25, 25, self.isMac)
        self.mouseMovement.moveToLocation(locationWheat)
        self.mouseMovement.leftClick()
        time.sleep(0.1)

        self.enterFeedingAmount()
        self.closeWindow()

    def acceptProductsIfThere(self):
        if hasFinishedAnimalProduct():
            locAcceptButton = getCoordinatesRGB("sc/constructionBuildings/finishAnimalProductAccept.png", 20, 20, self.isMac)
            self.mouseMovement.moveToLocation(locAcceptButton)
            self.mouseMovement.leftClick()
    
    def enterFeedingAmount(self):
        locEnterAmount = getCoordinatesRGB("sc/constructionBuildings/enterFeedingAmount.png", 50,15,self.isMac)
        if locEnterAmount == False:
            return
        print(locEnterAmount.getRandomXAndY())
        self.mouseMovement.moveToLocation(locEnterAmount)
        self.mouseMovement.leftClick()

        time.sleep(max(0.1, random.gauss(0.2,0.05)))


    def closeWindow(self):
        locClosingWindow = getCoordinatesRGB("sc/constructionBuildings/closeFarmButton.png", 10,10, self.isMac)
        self.mouseMovement.moveToLocation(locClosingWindow)
        self.mouseMovement.leftClick()
        time.sleep(max(0.13, random.gauss(0.22,0.04)))
