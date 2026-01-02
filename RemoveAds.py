from getCoordinates import *
from mouseMovement import *
def checkForAdds(isMac : bool, mouseMovement : MouseMovement, picturePath = "sc/constructionBuildings/closeFarmButton.png"):
    location = getCoordinatesRGB(picturePath, 20,20, isMac, 0.63)
    if location == False:
        print("No adds has been seen")
        return
    else:
        mouseMovement.moveToLocation(location)
        mouseMovement.leftClick()
        time.sleep(0.3)
        checkForAdds(isMac, mouseMovement)

time.sleep(4)
checkForAdds(True, MouseMovement())

    
    