from getCoordinates import *
from mouseMovement import MouseMovement

class Cow:
    def __init__(self, cowCount, onlyOneFoodSupply : bool, isMac :bool, mouseMovement : MouseMovement):
        self.cowCount = cowCount
        self.onlyOneFoodSupply = onlyOneFoodSupply
        self.isMac = isMac
        self.mouseMovement = mouseMovement

    def feedCows(self):
        locationFood = getCoordinatesRGB("sc/cow/foodForCows.png", 25, 25, self.isMac)
        self.mouseMovement.moveToLocation(locationFood)
        self.mouseMovement.leftClick()