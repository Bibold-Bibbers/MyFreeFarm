import math
import pyautogui
from mouseMovement import MouseMovement 
from Location import *
import numpy
import time
from CoordinatesLaptops import XYKoordinatenLabtops
import cv2
from InventoryManager import *



class Acker:
    #Time in Hours
    TIME_PLANT = {
        "test" : 8
    }

    def __init__(self, AckerPos : Location = None, startingCordinates : XYKoordinatenLabtops = None, isMac = True):
        self.AckerPos = AckerPos
        self.AckerRows = 10
        self.AckerColumns = 12
        self.startingPlantTime = None


        self.isMac = isMac
        self.startingCoordinates = self.setStartingXYFromAcker()
        self.ernteSymbolPos = self.setHarvestLoc()
        self.pflanzenSymbolPos = self.setPlantLoc()
        self.waterSymbolPos = self.setWaterLoc()

        self.mouseMovement = MouseMovement()
        self.inventoryManager = InventoryManager(startingCordinates)
        self.inventoryManager.searchForEntities()

        ###Zuerst Col dann row
        self.fieldArray = numpy.empty((self.AckerColumns, self.AckerRows), dtype=object)

        self.fillFullFieldArray()

    def fillFullFieldArray(self):
        startingX = self.startingCoordinates.getXStart()
        for col in range(self.AckerColumns):
            startingY = self.startingCoordinates.getYStart()
            for row in range(self.AckerRows):
                self.fieldArray[col][row] = SingleField(True, None, None, startingX, startingY, None)
                #print(f'col:{col+1} - row{row+1} - startX:{startingX} - startingY:{startingY}')
                startingY += 40
            startingX += 40

    def setStartingXYFromAcker(self):
        ###Noch anpassen das es direkt rein kommt
        screenshot = pyautogui.screenshot()
        target = cv2.imread('sc/acker/holeAcker.png')
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_lox= cv2.minMaxLoc(result)
        print("Acker")
        x,y = max_lox
        if (self.isMac == True): 
            x = x//2
            y = y//2
        print(max_val, max_lox)

        return Location(x,y, 25,30)
        



    def setPlantLoc(self):
        screenshot = pyautogui.screenshot()
        target = cv2.imread('sc/acker/plant.png')
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_lox= cv2.minMaxLoc(result)
        x,y = max_lox
        if (self.isMac == True): 
            x = x//2
            y = y//2
        print("Plant")
        print(max_val, max_lox)
        return Location(x,y, 25,30)

    def setWaterLoc(self):
        screenshot = pyautogui.screenshot()
        target = cv2.imread('sc/acker/water.png')
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_lox= cv2.minMaxLoc(result)
        x,y = max_lox
        if (self.isMac == True): 
            x = x//2
            y = y//2
        print("Water")
        print(max_val, max_lox)
        return Location(x,y, 25,30)
    
    def setHarvestLoc(self):
        screenshot = pyautogui.screenshot()
        target = cv2.imread('sc/acker/harvest.png')
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_lox= cv2.minMaxLoc(result)
        x,y = max_lox
        if (self.isMac == True): 
            x = x//2
            y = y//2
        print("Harvest")
        print(max_val, max_lox)
        return Location(x,y, 25,30)
            


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

        ##Old Function that uses locateOnScreen to get the plants
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
        screenLocate = pyautogui.locateOnScreen(plantImage, confidence=0.90)
        location = makeLocationWithPosition(screenLocate)
        x,y = location.getRandomXAndY()
        self.mouseMovement.moveTo(x,y)
        self.mouseMovement.leftClick()

    def checkEverySingleFieldForWeeds(self):
        fieldsFreeFromStuff = 0
        for row in range(self.AckerRows):
            for col in range(self.AckerColumns):
                fieldsFreeFromStuff += self.fieldArray[col][row].setIsFreeFromWeeds(row, col)
                #print(f'row: {row +1}, col: {col+1}, isFreeFromWeed: {self.fieldArray[col][row].getIsFreeFromWeeds()}')

        print(fieldsFreeFromStuff)

    def calculateCostToFreeField(self):
        totalCost = 0
        for row in range(self.AckerRows):
            for col in range(self.AckerColumns):
                cost = self.fieldArray[col][row].getPriceOfWeed()
                totalCost += cost
                #print(f'{self.fieldArray[col][row].getTypeOfWeed()} --- {cost} ----row:{row} -- col: {col}')
        print(totalCost)

    
    

    def harvestPlantWater(self, anbauPflanzePfad, withHarvest: bool =True, withWater: bool =True, withPlanting: bool =True):
        if withHarvest:
            self.goIntoHarvestMode()
            self.leftClickOnEveryFreeField()
        if withPlanting:
            self.goIntoPlantMode()
            self.inventoryManager.selectProduct('strawberr')
            self.leftClickOnEveryFreeField()
        if withWater:
            self.goIntoWaterMode()
            self.leftClickOnEveryFreeField()

    def leftClickOnEveryFreeField(self):
        for row in range(self.AckerRows):
            for col in range(self.AckerColumns):
                ##If it is free from Weed move to it and left click it
                #print(f'Field Col:{col}-Row{row} --- isFreeFromWeed {self.fieldArray[col][row].getIsFreeFromWeeds()} ')

                if self.fieldArray[col][row].getIsFreeFromWeeds():
                    x = self.fieldArray[col][row].getXBegin()
                    y = self.fieldArray[col][row].getYBegin()
                    location = Location(x,y,40,40)
                    x,y = location.getRandomXAndY()
                    self.mouseMovement.moveToAndLeftClick(x,y)
                    #self.mouseMovement.moveTo(x,y)
            

class SingleField:

    WEED_COST = {
        "sc/acker/grassGrey.png" : 2.5,
        "sc/acker/darkStoneGrey.png" : 30,
        "sc/acker/whiteStoneGrey.png" : 180,
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
            if (highestScore < 0.4):
                self.isFreeFromWeeds = True
                #print(f'Hier ist ein Tile das nicht erkannt wurde - row:{row+1}, col{col+1}, confidence:{highestScore} ----- Best Bild:{best_bild}')
                return 1
            else:
                self.isFreeFromWeeds = False
                self.typeOfWeed = best_bild
                return 0
            
    def getPriceOfWeed(self):
        return self.WEED_COST.get(self.typeOfWeed, 0)
    
    def getTypeOfWeed(self):
        return self.typeOfWeed


    def getIsFreeFromWeeds(self):
        return self.isFreeFromWeeds

    def getXBegin(self):
        return int(self.xBegin)
    
    def getYBegin(self):
        return int(self.yBegin)






