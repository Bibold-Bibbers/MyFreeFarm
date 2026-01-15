import json
import pyautogui
import cv2
import numpy as np
import time
from location import Location
from coordinatesLaptops import XYKoordinatenLabtops
from mouseMovement import MouseMovement


class InventoryManager:
    def __init__(self, laptop : XYKoordinatenLabtops):
        self.products = []
        self.mouseMovement = MouseMovement()
        self.laptop = laptop
        with open("config/products.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        for name, path in data["products"].items():
            self.products.append(Product(name, 0, path))

    def searchForEntities(self):
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        for product in self.products:
            templatePath = product.getPath()
            template = cv2.imread(templatePath)
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, maxloc = cv2.minMaxLoc(result)
            if (max_val < 0.7):
                print(f'Fehler InventoryManager for product {product.name}')
            x, y = maxloc
            if self.laptop.getIsMac():
                x = int(x/2)
                y = int(y/2)
            product.setLocation(Location(x,y, width=30, height=30))

    def selectProduct(self, name):
        for product in self.products:
            if product.getName() == name:
                x,y = product.getLocation().getRandomXAndY()
                self.mouseMovement.moveToAndLeftClick(x,y)
      
    
class Product:
    def __init__(self, name, quantity, path):
        self.name = name
        self.quantity = quantity
        self.path = path
        self.location = None

    def getName(self):
        return self.name
    
    def setQuantity(self, newQuantity):
        self.quantity = newQuantity
    
    def getQuantity(self):
        return self.quantity
    
    def getPath(self):
        return self.path
    
    def setLocation(self, location):
        self.location = location
    
    def getLocation(self):
        return self.location

