import pyautogui 
import time
import keyboard 
import win32api, win32con

from pyautogui import *

#appuyer sur a pour commencer et q pour stopper

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def auto():
	while not keyboard.is_pressed('q'):
		screen = pyautogui.screenshot(region=(552,220, 800, 400))
		w,h = screen.size
		for x in range (0,w,10):
			br = False
			for y in range(0,h,10):
				r,g,b = screen.getpixel((x,y))
				if r == 149: ##couleur en 'rouge' du blanc utiilisé pour les cibles
					click(x+552,y+220)
					time.sleep(0.01)
					br = True
					break
			if br :
				break

try:
	while 1:
		if not keyboard.is_pressed("a"):
			sleep(1)
		else :
			auto()
except KeyboardInterrupt:
	print("Session fini")


