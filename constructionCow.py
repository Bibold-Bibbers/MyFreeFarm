from getCoordinates import *
from mouseMovement import MouseMovement
import time 
import random

class Cow:
    def __init__(self, cowCount, onlyOneFoodSupply : bool, isMac :bool, mouseMovement : MouseMovement):
        self.cowCount = cowCount
        self.onlyOneFoodSupply = onlyOneFoodSupply
        self.isMac = isMac
        self.mouseMovement = mouseMovement

    def feedCows(self):
        self.acceptProductsIfThere()
        locationFood = getCoordinatesRGB("sc/cow/foodForCows.png", 25, 25, self.isMac)
        print(locationFood)
        self.mouseMovement.moveToLocation(locationFood)
        self.mouseMovement.leftClick()
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