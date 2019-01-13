# coding: utf-8
import os
import time
from PIL import ImageGrab

"""ScreenGrab
On firefox fullscreen 100% on 1920x1080res on top of the web page
 """
def screenGrab():
    x_pad = 464
    y_pad = 226
    box = (x_pad+1,y_pad +1,x_pad+640,y_pad + 480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time()))+'.png','PNG')

def main():
	screenGrab()

if __name__ == "__main__":
	main()
