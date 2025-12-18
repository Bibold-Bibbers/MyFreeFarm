import math
import pyautogui
from mouseMovement import MouseMovement 
from locationVariable import *
import numpy
import time



class Acker:
    def __init__(self, AckerPos : Location, ernteSymbolPos : Location, pflanzenSymbolPos : Location, waterSymbolPos : Location):
        self.AckerPos = AckerPos
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
            startingX = 855
            for col in range(self.AckerColumns):
                startingY = 460
                for row in range(self.AckerRows):
                    self.fieldArray[col][row] = SingleField(True, None, None, startingX, startingY, None)
                    startingY += 40
                startingX += 40
        else:
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
        for row in range(6):
            for col in range(7):
                x = self.fieldArray[col][row].getXBegin()
                y = self.fieldArray[col][row].getYBegin()
                print(x)
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

    def clickOnFields(self):
        startX = 943
        startY = 480
        stopX = 1215
        stopY = 711
        diffX = (stopX - startX)
        diffY = (stopY - startY)
        width, height = 40, 40
        




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
    def __init__(self, isFreeFromWeeds, currentCrop, currentCropPlantedTime, xBegin, yBegin, connectedCrop):
        self.isFreeFromWeeds = isFreeFromWeeds
        self.currentCrop = currentCrop
        self.currentCropPlantedTime = currentCropPlantedTime
        self.xBegin = xBegin
        self.xEnd = xBegin + 35
        self.yBegin = yBegin
        self.yEnd = yBegin + 35
        self.connenctedCrop = connectedCrop

    def getXBegin(self):
        return int(self.xBegin)
    
    def getYBegin(self):
        return int(self.yBegin)




