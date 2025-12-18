class Location:
    def __init__(self, x, y, width, height):
        self.xMin = x
        self.yMin = y
        self.xMax = x + width
        self.YMax = y + height

    def getRandomXAndY(self):
        xRandom = (self.xMax + self.xMin)/2
        yRandom = (self.yMin + self.YMax)/2
        return xRandom, yRandom
    

def makeLocationWithPosition(position):
    x = position.left
    y = position.top
    width = position.width
    height = position.height
    return Location(x,y,width,height)

