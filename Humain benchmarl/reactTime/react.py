import pyautogui 
import time
import keyboard 
import win32api, win32con 

from pyautogui import *
from time import sleep


#q pour quitter

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def auto(): ##clique lorsque du vert apparait
	while not keyboard.is_pressed('q'):
		screen = pyautogui.screenshot(region=(190,190,210,210))
		x = 200
		y = 200
		r,g,b = screen.getpixel((x,y))
		if g == 219: #couleur du vert utiliser lorsque l'on doit réagir
			print("click")
			click(500,500)
			br = True
			break

while not keyboard.is_pressed('q'):
	auto()