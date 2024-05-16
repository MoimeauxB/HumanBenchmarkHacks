import pyautogui
import keyboard
import easyocr as ocr

from pyautogui import *
from time import sleep 

##Parfois le curseur qui indique que l'on peut écrire est lu comme un 'I' malheureusement ce phénomène est inconsistant ce qui le rend difficile à corriger

reader = ocr.Reader(['en'])
sleep(1)
screen = pyautogui.screenshot("TextToConvert.png",region=(502,386,967,200)) #plus ou moins la boite la plus large de text rencontrée en 15 essais
result = reader.readtext('TextToConvert.png')

text = ""
for r in result:
	text += r[1]+" "

print("text reconnu : \n", text,"\n\n")

def write(text):
	for l in text:
		pyautogui.write(l)


write(text)