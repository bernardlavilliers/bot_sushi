# coding: utf-8
import os
import sys
import time
import win32api, win32con
import pyautogui
from PIL import ImageGrab,ImageOps
from numpy import *
import pdb
import logging
import time
import random
import copy



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')

x_pad = 0
y_pad = 0
def locateGame():
    im = ImageGrab.grab()
    try:
        (x,y,w,h) = pyautogui.locateOnScreen('upperleftcorner.png')
    except pyautogui.pyscreeze.ImageNotFoundException :
        (x,y,w,h) = pyautogui.locateOnScreen('upperleftcorner2.png')
    print(x,y,file=sys.stderr)

    return (x-1,y-1)

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

class Cord:
    f_shrimp = ( 38, 339 )
    f_rice = ( 96, 339 )
    f_nori = ( 36, 386 )
    f_roe = ( 90, 394 )
    f_salmon = ( 40,445 )
    f_unagi = ( 89, 445 )

    phone = (564,390)

    menu_rice = (551,295)
    buy_rice = (547,284)

    menu_toppings = (522,274)

    t_shrimp = (487,224)
    t_unagi = (584,226)
    t_nori = (495,275)
    t_roe = (577,276)
    t_salmon = (494,332)

    t_exit = (589,343)

    delivery_norm = (495,297)

    f_plate1 = ( 95, 209 )
    f_plate2 = ( 193, 209 )
    f_plate3 = ( 294, 211 )
    f_plate4 = ( 387, 212 )
    f_plate5 = ( 496, 213 )
    f_plate6 = ( 605, 212 )

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.",file=sys.stderr)          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down',file=sys.stderr)

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release',file=sys.stderr)

def mousePos(cord):
    print(x_pad,y_pad,file=sys.stderr)
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print( x,y , file=sys.stderr)

def startGame():
    #location of first menu
    mousePos((317, 206))
    leftClick()
    time.sleep(.1)

    #location of second menu
    mousePos((314,392))
    leftClick()
    time.sleep(.1)

    #location of third menu
    mousePos((582,456))
    leftClick()
    time.sleep(.1)

    #location of fourth menu
    mousePos((316,380))
    leftClick()
    time.sleep(.1)
"""ScreenGrab
On firefox fullscreen 100% on 1920x1080res on top of the window
 """
def screenGrab():
    # x_pad = 464
    # y_pad = 226
    box = (x_pad+1,y_pad +1,x_pad+640,y_pad + 480)
    im = ImageGrab.grab(box)
    # im.save(os.getcwd() + '\\full_snap__' + str(int(time.time()))+'.png','PNG')
    return im

def makeFood(food):
    if food == 'caliroll':
        print( 'Making a caliroll',file=sys.stderr)
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print('Making a onigiri',file=sys.stderr)
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)

        time.sleep(1.5)

    elif food == 'gunkan':
        print('Making a gunkan',file=sys.stderr)
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
def clear_tables():
    mousePos(Cord.f_plate1)
    leftClick()

    mousePos(Cord.f_plate2)
    leftClick()

    mousePos(Cord.f_plate3)
    leftClick()

    mousePos(Cord.f_plate4)
    leftClick()

    mousePos(Cord.f_plate5)
    leftClick()

    mousePos(Cord.f_plate6)
    leftClick()
    time.sleep(1)

def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)

def buyFood(food):

    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            print('rice is available',file=sys.stderr)
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('rice is NOT available',file=sys.stderr)
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)



    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print( 'test',file=sys.stderr)
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (33, 30, 11):
            print('nori is available',file=sys.stderr)
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('nori is NOT available',file=sys.stderr)
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (127, 61, 0):
            print('roe is available',file=sys.stderr)
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('roe is NOT available',file=sys.stderr)
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print('{} is low and needs to be replenished'.format(i))
                buyFood(i)

def main():
    startGame()

if __name__ == "__main__":
    x_pad,y_pad = locateGame()
    print(x_pad,y_pad,"main passedaa")
    main()
