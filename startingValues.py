from locationVariable import *

class XYKoordinatenLabtops:

    def __init__(self, isMac, xStart, xEnd, yStart, yEnd, xBrowserSearch, yBroserSearch, xLoginStart, loginWidth, yLoginStart,loginHeight, xLoginPWStart, yLoginPWStart, xLoginButton, yLoginButton):
        self.isMac = isMac
        
        self.xStart = xStart + 5
        self.xEnd = xEnd - 5
        self.yStart = yStart + 5
        self.yEnd = yEnd -5

        ##Browser Location of search bar
        self.xBrowserSearch = xBrowserSearch
        self.yBroswerSearch = yBroserSearch


        ##X start is for clarity about 5 pixel inwards, and Y is 2
        ##  width have 10 less and height has 4
        self.xLoginStart = xLoginStart
        self.loginWidth = loginWidth
        self.yLoginStart = yLoginStart
        self.loginHeight = loginHeight
        self.xLoginPWStart = xLoginPWStart
        self.yLoginPWStart = yLoginPWStart        

        ##Login Button is about the size of loginHeight
        self.xLoginButton = xLoginButton
        self.yLoginButton = yLoginButton

    def getIsMac(self):
        return self.isMac
    
    def getXStart(self):
        return int(self.xStart)
    
    def getYStart(self):
        return int(self.yStart)
    
    def getYBrowserSearch(self):
        return int(self.yBroswerSearch)
    
    def getXBroswerSearch(self):
        return int(self.xBrowserSearch)
    
    def getLoginRandominizedXY(self):
        locationLogin = Location(self.xLoginStart +5, self.yLoginStart +2, self.loginWidth-10, self.loginHeight-4)
        x,y = locationLogin.getRandomXAndY()
        return x,y
    
    def getLoginPWRandominizedXY(self):
        locationPWLogin = Location(self.xLoginPWStart +5, self.yLoginPWStart +2, self.loginWidth -10, self.loginHeight-4)
        x,y = locationPWLogin.getRandomXAndY()
        return x,y
    
    def getLoginButtonRandomizedXY(self):
        ##width and height of the button are about the size of the loginHeight
        locationLoginButton = Location(self.xLoginButton, self.yLoginButton, self.loginHeight, self.loginHeight)
        x,y = locationLoginButton.getRandomXAndY()
        return x,y