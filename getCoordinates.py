from Location import Location
import pyautogui
import cv2
import numpy as np


def hasFinishedAnimalProduct():
    screenshot = pyautogui.screenshot()
    target = cv2.imread("sc/constructionBuildings/finishAnimalProduct.png")
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
    _, max_val, _,_ = cv2.minMaxLoc(result)
    print(max_val)
    if(max_val > 0.8):
        return True
    return False


def getCoordinatesRGB(target_path, width, height, isMac, confidence = 0.8):
    screenshot = pyautogui.screenshot()
    print(target_path)
    target = cv2.imread(target_path)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_lox= cv2.minMaxLoc(result)
    if max_val < confidence:
        print(f'Hier ist die Confidence unter max_val-targetPath:{target_path}-confidence:{confidence} - Es wird False Returned - Das ist die max_val: {max_val}')
        return False

    x,y = max_lox
    if (isMac == True): 
        x = x//2
        y = y//2
    print(max_val, max_lox)
    return Location(x,y, width=width, height=height)


def getAllCoordinatesRGB(target_path, width, height, isMac, confidence):
    screenshot = pyautogui.screenshot()
    target = cv2.imread(target_path)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
    
    threshold = confidence
    locations = np.where(result >= threshold)
    
    # 1. Alle gefundenen Punkte als Rechtecke sammeln
    rects = []
    for pt in zip(*locations[::-1]):
        # Wir fügen jedes Rechteck 2x hinzu, damit groupRectangles es nicht löscht
        rects.append([int(pt[0]), int(pt[1]), int(width), int(height)])
        rects.append([int(pt[0]), int(pt[1]), int(width), int(height)])

    # 2. Überlappende Rechtecke gruppieren
    # 1 = Mindestanzahl an Rechtecken pro Gruppe; 0.2 = Toleranz für Überlappung
    grouped_rects, weights = cv2.groupRectangles(rects, 1, 0.2)
    
    final_locations = []
    
    # 3. Ergebnisse in Location-Objekte umwandeln
    for (x, y, w, h) in grouped_rects:
        if isMac:
            x = x // 2
            y = y // 2
            
        final_locations.append(Location(x, y, width=width, height=height))
        print(f"Gefunden bei X: {x} - Y: {y}")

    return final_locations