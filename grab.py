# coding: utf-8
import os
import time
import ImageGrab

def screenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time()))+'.png','PNG')

def main():
	pass

if __name__ == "__main__":
	main()
