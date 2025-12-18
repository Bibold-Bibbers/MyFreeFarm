import math
import pyautogui
from mouseMovement import MouseMovement 
from locationVariable import *
import numpy

class Acker:
    def __init__(self, AckerPos : Location, ernteSymbolPos : Location, pflanzenSymbolPos : Location, waterSymbolPos : Location):
        self.AckerPos = AckerPos
        self.ernteSymbolPos = ernteSymbolPos
        self.pflanzenSymbolPos = pflanzenSymbolPos
        self.waterSymbolPos = waterSymbolPos
        self.mouseMovement = MouseMovement()

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
        tilesX = math.floor(diffX/40.0) + 1
        tilesY = math.floor(diffY/40.0) + 1
        counterX, counterY = 0, 0
        for i in range(tilesX):
            for z in range(tilesY):
                location = Location((startX + width * counterX), (startY + height * counterY), width, height)
                x,y = location.getRandomXAndY()
                self.mouseMovement.moveTo(x,y)
                self.mouseMovement.leftClick()
                counterY += 1
            counterX += 1
            counterY = 0




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
        



