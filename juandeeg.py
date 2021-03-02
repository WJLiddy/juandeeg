import time
import keyboard
import mouse
import math

import numpy as np
from PIL import ImageGrab
import cv2rr

template = cv2.imread('radar.png')

waypoints = [[83,302],[83,250],[99,212],[99,212],[r100,180],[79,180],[82,124],[115,90]]

waypoint_idx = 0
# bind "o" "+left
# bind "p" "+right

#run at 1280/720

# Set mouse position and unfreeze the game
mouse.move(100, 100, True)
mouse.click()
keyboard.press_and_release('esc')
time.sleep(1)

# In case the script was killed, release all the keys
keyboard.release("W")
keyboard.release("A")
keyboard.release("S")
keyboard.release("D")
keyboard.release("O")
keyboard.release("P")

# Functions

def getCoord():
    printscreen_pil = ImageGrab.grab(bbox=(50,120,50+100,120+100))
    open_cv_image = np.array(printscreen_pil) 
    # Convert RGB to BGR 
    img = open_cv_image[:, :, ::-1].copy() 

    method = cv2.TM_SQDIFF_NORMED
    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return min_loc

# hold down "P" and orient north, by checking for the lil arrow above the map.
def orientNorth():
    a = getCoord()
    keyboard.press("W")
    time.sleep(1)
    keyboard.release("W")
    b = getCoord()
    r = np.subtract(a,b)
    ang = math.atan2(r[1],r[0])

    rotspeed = 3.7
    targ = 3.1416 * (2.5)
    keyboard.press("P")
    time.sleep((targ - ang) / rotspeed)
    keyboard.release("P")


def inBuyTime():
    px = ImageGrab.grab().load()
    sumcol = 0
    for x in range(624,624+2):
        for y in range(43,43+11):
            if(px[x,y][0] == 255 and px[x,y][1] != 255):
                return True
    return False


#Buy deeg,
keyboard.press_and_release("B")
time.sleep(0.05)
keyboard.press_and_release("3")
time.sleep(0.05)
keyboard.press_and_release("4")
time.sleep(0.05)
keyboard.press_and_release("1")
time.sleep(0.05)
keyboard.press_and_release("5")
time.sleep(0.05)
keyboard.press_and_release("B")
time.sleep(0.05)


# Wait for round to start.
while(inBuyTime()):
    time.sleep(0.01)

orientNorth()


while True:
    time.sleep(0.5)
    keyboard.release("W")
    keyboard.release("A")
    keyboard.release("S")
    keyboard.release("D")
    keyboard.press_and_release("2")
    keyboard.press_and_release("1")
    mouse.click()r
    keyboard.press_and_release("R")

    a = getCoord()
    dist = np.subtract(waypoints[waypoint_idx],a)
    print(dist)
    if(dist[0] > 0):
        keyboard.press("D")
    elif(dist[0] < 0):
        keyboard.press("A")

    if(dist[1] > 0):
        keyboard.press("S")
    elif(dist[1] < 0):
        keyboard.press("W")

    if(np.linalg.norm(dist) < 6):
        waypoint_idx += 1

    if(waypoint_idx == len(waypoints)):    
        keyboard.release("W")
        keyboard.release("A")
        keyboard.release("S")
        keyboard.release("D")
        break


keyboard.press("E")
time.sleep(6)
keyboard.release("E")

keyboard.press("S")
time.sleep(4)
keyboard.release("S")

while True:
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    keyboard.press_and_release("R")


