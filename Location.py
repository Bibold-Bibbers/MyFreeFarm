import random

class Location:
    def __init__(self, x, y, width, height):
        self.xMin = x
        self.yMin = y
        self.xMax = x + width
        self.YMax = y + height
        self.width = width
        self.height = height

    def getRandomXAndY(self):
        mu_x = (self.xMax + self.xMin)/2
        mu_y = (self.yMin + self.YMax)/2

        sigma_x = self.width/6
        sigma_y = self.height/6

        target_x = random.gauss(mu_x, sigma_x)
        target_y =random.gauss(mu_y, sigma_y)
        
        target_x = max(self.xMin + 2, min(target_x, self.xMax - 2))
        target_y = max(self.yMin + 2, min(target_y, self.YMax - 2))

        return target_x, target_y
    
    def getXStart(self):
        return self.xMin
    
    def getYStart(self):
        return self.yMin
    

def makeLocationWithPosition(position):
    x = position.left
    y = position.top
    width = position.width
    height = position.height
    return Location(x,y,width,height)

