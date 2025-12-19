import math
import pyautogui
from mouseMovement import MouseMovement 
from Location import *
import numpy
import time
from CoordinatesLaptops import XYKoordinatenLabtops
import cv2



class Acker:
    def __init__(self, AckerPos : Location, ernteSymbolPos : Location, pflanzenSymbolPos : Location, waterSymbolPos : Location, startingCordinates : XYKoordinatenLabtops):
        self.AckerPos = AckerPos
        self.startingCoordinates = startingCordinates
        self.AckerRows = 10
        self.AckerColumns = 12
        self.ernteSymbolPos = ernteSymbolPos
        self.pflanzenSymbolPos = pflanzenSymbolPos
        self.waterSymbolPos = waterSymbolPos
        self.mouseMovement = MouseMovement()
        self.fieldArray = numpy.empty((self.AckerColumns, self.AckerRows), dtype=object)

        self.fillFullFieldArray(True)

    def fillFullFieldArray(self, full :bool):
        if full:
            startingX = self.startingCoordinates.getXStart()
            for col in range(self.AckerColumns):
                startingY = self.startingCoordinates.getYStart()
                for row in range(self.AckerRows):
                    self.fieldArray[col][row] = SingleField(True, None, None, startingX, startingY, None)
                    startingY += 40
                startingX += 40
        else:
            ##Muss noch angepasst werden mit den startingCoordinates
            AckerRows = 6
            AckerColumns = 7
            startingX = 930
            for col in range(AckerColumns):
                startingY = 460
                for row in range(AckerRows):
                    self.fieldArray[col][row] = SingleField(True, None, None, startingX, startingY, None)
                    startingY += 40
                startingX += 40
            


    def testFieldXY(self):

        ##wenn es das ganze Feld ist muss die Range mehr sein
        for row in range(10):
            for col in range(12):
                x = self.fieldArray[col][row].getXBegin()
                y = self.fieldArray[col][row].getYBegin()
                print(f'x:{x} y:{y}  col:{col}, row:{row}')
                self.mouseMovement.moveTo(x,y)
                time.sleep(1)

    def fromFarmToAcker(self):
        self.mouseMovement.moveToLocation(self.AckerPos)
        self.mouseMovement.leftClick()

    def erntePflanzen(self, pflanzenScreenshot):
        position = pyautogui.locateAllOnScreen(pflanzenScreenshot, confidence=0.9)
        for pflanze in position:
            locationPflanze = makeLocationWithPosition(pflanze)
            x,y = locationPflanze.getRandomXAndY()
            self.mouseMovement.moveTo(x,y)
            self.mouseMovement.leftClick()
            
    def goIntoHarvestMode(self):
       self.mouseMovement.moveToLocation(self.ernteSymbolPos)
       self.mouseMovement.leftClick() 

    def goIntoPlantMode(self):
       self.mouseMovement.moveToLocation(self.pflanzenSymbolPos)
       self.mouseMovement.leftClick() 

    def goIntoWaterMode(self):
        self.mouseMovement.moveToLocation(self.waterSymbolPos)
        self.mouseMovement.leftClick()
       
    def selectPlant(self, plantImage):
        screenLocate = pyautogui.locateOnScreen(plantImage, confidence=0.95)
        location = makeLocationWithPosition(screenLocate)
        x,y = location.getRandomXAndY()
        self.mouseMovement.moveTo(x,y)
        self.mouseMovement.leftClick()

    def checkEverySingleField(self):
        fieldsFreeFromStuff = 0
        for row in range(self.AckerRows):
            for col in range(self.AckerColumns):
                fieldsFreeFromStuff += self.fieldArray[col][row].setIsFreeFromWeeds(row, col)
                #print(f'row: {row +1}, col: {col+1}, isFreeFromWeed: {self.fieldArray[col][row].getIsFreeFromWeeds()}')

        print(fieldsFreeFromStuff)


    def harvestPlantWater(self, fertigePflanzenPfad, anbauPflanzePfad, withHarvest: bool =True, withWater: bool =True, withPlanting: bool =True):
        if withHarvest:
            self.goIntoHarvestMode()
            for pflanzePfad in fertigePflanzenPfad:
                self.erntePflanzen(pflanzePfad)
        if withPlanting:
            self.goIntoPlantMode()
            self.selectPlant(anbauPflanzePfad)
            self.clickOnFields()
        if withWater:
            self.goIntoWaterMode()
            self.clickOnFields()
        


class SingleField:

    WEED_COST = {
        "sc/acker/grassGrey.png" : 2.5,
        "sc/acker/darkStoneGrey.png" : 30,
        "sc/acker/whiteStone.png" : 180,
        "sc/acker/bugsGrey.png" : 500
    }

    def __init__(self, isFreeFromWeeds, currentCrop, currentCropPlantedTime, xBegin, yBegin, connectedCrop):
        self.isFreeFromWeeds = isFreeFromWeeds
        self.typeOfWeed = None
        self.currentCrop = currentCrop
        self.currentCropPlantedTime = currentCropPlantedTime
        self.xBegin = xBegin
        self.xEnd = xBegin + 35
        self.yBegin = yBegin
        self.yEnd = yBegin + 35
        self.connenctedCrop = connectedCrop

    def getConfidenceFromTwoPictures(self, pictureLink, screenshot):
        pictureField = cv2.imread(pictureLink, 0)
        if pictureField is None: return 0
        res = cv2.matchTemplate(screenshot,pictureField, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)
        return max_val
    
    
    def setIsFreeFromWeeds(self, row, col):
        vergleichsBilder = ["sc/acker/bugsGrey.png","sc/acker/darkStoneGrey.png","sc/acker/grassGrey.png","sc/acker/whiteStoneGrey.png","sc/acker/emptyTileGrey.png"]
        screenshot = pyautogui.screenshot(region=(self.xBegin - 5, self.yBegin-3, 40, 40))
        screenshot_cv = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2GRAY)
        cv2.imwrite(f'screenshotsAcker/{row}-{col}-gray.png', screenshot_cv)
        highestScore = 0
        best_bild = None
        for bild in vergleichsBilder:
            conf = self.getConfidenceFromTwoPictures(bild, screenshot_cv)
            if conf > highestScore:
                highestScore = conf
                best_bild = bild
        #print(f'{best_bild} confidence: {highestScore}')
        if (best_bild == "sc/acker/emptyTileGrey.png"):
            self.isFreeFromWeeds = True
            return 1
        else:
            if (highestScore < 0.5):
                self.isFreeFromWeeds = True
                print(f'Hier ist ein Tile das nicht erkannt wurde - row:{row+1}, col{col+1}, confidence:{highestScore} ----- Best Bild:{best_bild}')
                return 1
            else:
                self.isFreeFromWeeds = False
                self.typeOfWeed = best_bild
                return 0
            
    def getPriceOfWeed(self):
        return self.WEED_COST[self.typeOfWeed, 0]


    def getIsFreeFromWeeds(self):
        return self.isFreeFromWeeds

    def getXBegin(self):
        return int(self.xBegin)
    
    def getYBegin(self):
        return int(self.yBegin)






