import os
import time
import pyautogui
import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom


##from flask import Flask, request
##import json
##import requests
##import redis

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		##possibly use this? data['message']
		##submittedText = message.replace("/speech ","",1)
		##if message.startswith("/speech "):
		for line in temp:
			print(line)
                        user = getUser(line)
                        message = getMessage(line)
                        pyautogui.size()
			(1366, 768)
                        if "a" in message:
                                pyautogui.typewrite('a')
                                break
                        if "b" in message:
                                pyautogui.typewrite('b')
                                break
                        if "c" in message:
                                pyautogui.typewrite('c')
                                break
                        if "d" in message:
                                pyautogui.typewrite('d')
                                break
                        if "e" in message:
                                pyautogui.typewrite('e')
                                break
                        if "f" in message:
                                pyautogui.typewrite('f')
                                break
                        if "g" in message:
                                pyautogui.typewrite('g')
                                break
                        if "h" in message:
                                pyautogui.typewrite('h')
                                break
                        if "i" in message:
                                pyautogui.typewrite('i')
                                break
                        if "j" in message:
                                pyautogui.typewrite('j')
                                break
                        if "k" in message:
                                pyautogui.typewrite('k')
                                break
                        if "l" in message:
                                pyautogui.typewrite('l')
                                break
                        if "m" in message:
                                pyautogui.typewrite('m')
                                break
                        if "n" in message:
                                pyautogui.typewrite('n')
                                break
                        if "o" in message:
                                pyautogui.typewrite('o')
                                break
                        if "p" in message:
                                pyautogui.typewrite('p')
                                break
                        if "q" in message:
                                pyautogui.typewrite('q')
                                break
                        if "r" in message:
                                pyautogui.typewrite('r')
                                break
                        if "s" in message:
                                pyautogui.typewrite('s')
                                break
                        if "t" in message:
                                pyautogui.typewrite('t')
                                break
                        if "u" in message:
                                pyautogui.typewrite('u')
                                break
                        if "v" in message:
                                pyautogui.typewrite('v')
                                break
                        if "w" in message:
                                pyautogui.typewrite('w')
                                break
                        if "x" in message:
                                pyautogui.typewrite('x')
                                break
                        if "y" in message:
                                pyautogui.typewrite('y')
                                break
                        if "z" in message:
                                pyautogui.typewrite('z')
                                break
## Capitals
                        if "A" in message:
                                pyautogui.typewrite('A')
                                break
                        if "B" in message:
                                pyautogui.typewrite('B')
                                break
                        if "C" in message:
                                pyautogui.typewrite('C')
                                break
                        if "D" in message:
                                pyautogui.typewrite('D')
                                break
                        if "E" in message:
                                pyautogui.typewrite('E')
                                break
                        if "F" in message:
                                pyautogui.typewrite('F')
                                break
                        if "G" in message:
                                pyautogui.typewrite('G')
                                break
                        if "H" in message:
                                pyautogui.typewrite('H')
                                break
                        if "I" in message:
                                pyautogui.typewrite('I')
                                break
                        if "J" in message:
                                pyautogui.typewrite('J')
                                break
                        if "K" in message:
                                pyautogui.typewrite('K')
                                break
                        if "L" in message:
                                pyautogui.typewrite('L')
                                break
                        if "M" in message:
                                pyautogui.typewrite('M')
                                break
                        if "N" in message:
                                pyautogui.typewrite('N')
                                break
                        if "O" in message:
                                pyautogui.typewrite('O')
                                break
                        if "P" in message:
                                pyautogui.typewrite('P')
                                break
                        if "Q" in message:
                                pyautogui.typewrite('Q')
                                break
                        if "R" in message:
                                pyautogui.typewrite('R')
                                break
                        if "S" in message:
                                pyautogui.typewrite('S')
                                break
                        if "T" in message:
                                pyautogui.typewrite('T')
                                break
                        if "U" in message:
                                pyautogui.typewrite('U')
                                break
                        if "V" in message:
                                pyautogui.typewrite('V')
                                break
                        if "W" in message:
                                pyautogui.typewrite('W')
                                break
                        if "X" in message:
                                pyautogui.typewrite('X')
                                break
                        if "Y" in message:
                                pyautogui.typewrite('Y')
                                break
                        if "Z" in message:
                                pyautogui.typewrite('Z')
                                break
                        if "1" in message:
                                pyautogui.typewrite('1')
                                break
                        if "2" in message:
                                pyautogui.typewrite('2')
                                break
                        if "3" in message:
                                pyautogui.typewrite('3')
                                break
                        if "4" in message:
                                pyautogui.typewrite('4')
                                break
                        if "5" in message:
                                pyautogui.typewrite('5')
                                break
                        if "6" in message:
                                pyautogui.typewrite('6')
                                break
                        if "7" in message:
                                pyautogui.typewrite('7')
                                break
                        if "8" in message:
                                pyautogui.typewrite('8')
                                break
                        if "9" in message:
                                pyautogui.typewrite('9')
                                break
                        if "0" in message:
                                pyautogui.typewrite('0')
                                break
                        if "!" in message:
                                pyautogui.typewrite('!')
                                break
                        if "@" in message:
                                pyautogui.typewrite('@')
                                break
                        if "#" in message:
                                pyautogui.typewrite('#')
                                break
                        if "$" in message:
                                pyautogui.typewrite('$')
                                break
                        if "%" in message:
                                pyautogui.typewrite('%')
                                break
                        if "^" in message:
                                pyautogui.typewrite('^')
                                break
                        if "&" in message:
                                pyautogui.typewrite('&')
                                break
                        if "*" in message:
                                pyautogui.typewrite('*')
                                break
                        if "(" in message:
                                pyautogui.typewrite('(')
                                break
                        if ")" in message:
                                pyautogui.typewrite(')')
                                break		
				
				
				
				
				
				
                        if "`" in message:
                                pyautogui.typewrite('`')
                                break
                        if "~" in message:
                                pyautogui.typewrite('~')
                                break
                        if "[" in message:
                                pyautogui.typewrite('[')
                                break
                        if "]" in message:
                                pyautogui.typewrite(']')
                                break
                        if "{" in message:
                                pyautogui.typewrite('{')
                                break
                        if "}" in message:
                                pyautogui.typewrite('}')
                                break
                        if "'\'" in message:
                                pyautogui.typewrite('\')
                                break
                        if "|" in message:
                                pyautogui.typewrite('|')
                                break
                        if ":" in message:
                                pyautogui.typewrite(':')
                                break
                        if ";" in message:
                                pyautogui.typewrite(';')
                                break
                        if "-" in message:
                                pyautogui.typewrite('-')
				break
			if "'" in message:
                                pyautogui.typewrite("'")
				break
                        if "," in message:
                                pyautogui.typewrite(',')
                                break
                        if "<" in message:
                                pyautogui.typewrite('<')
                                break
                        if "." in message:
                                pyautogui.typewrite('.')
                                break
                        if ">" in message:
                                pyautogui.typewrite('>')
                                break
                        if "/" in message:
                                pyautogui.typewrite('/')
                                break
                        if "+" in message:
                                pyautogui.typewrite('+')
                                break
                        if "=" in message:
                                pyautogui.typewrite('=')
                                break
				
				
				
				##This is the Symbols
##This needs to be a string of characters like ctrl+alt+g or something to this extent
##Using japanese characters as substitute because all other american/european letters are taken
##Character " し " will be used as enter
                        if "し" in message:
                                pyautogui.hotkey('enter')

				##keep the terminal in the normal spot
				##right click the top of the terminal window and click always on top
				##this is the "paste into twitchchat" part of the script
				##might just get rid of this part of the script
				pyautogui.moveTo(392, 206)
				pyautogui.click(clicks=1)
				pyautogui.moveTo(399, 290)
				pyautogui.click(clicks=1)
				pyautogui.click(button='right')
				pyautogui.moveTo(440, 370)
				pyautogui.click(button='right')
				pyautogui.moveTo(1037, 599)
				pyautogui.click(button='right')
				pyautogui.moveTo(1061, 416)
				pyautogui.click(clicks=1)
				pyautogui.hotkey('enter')
				pyautogui.moveTo(634, 379)
				pyautogui.click(clicks=1)

				break



				##add extras for capitals, symbols and numbers
##This is the "refresh" character to print the current terminal screen
##Making the pasting option be also having the copying the small sized terminal is an option too
##Possibly make the 

##Refresh character " ぁ " is used to show the newest screen for the terminal
                        if "ぁ" in message:
		
				##keep the terminal in the normal spot
				##right click the top of the terminal window and click always on top
				##this is the "paste into twitchchat" part of the script
				##make this it's own command? possibly use different characters?
				pyautogui.moveTo(392, 206)
				pyautogui.click(clicks=1)
				pyautogui.moveTo(399, 290)
				pyautogui.click(clicks=1)
				pyautogui.click(button='right')
				pyautogui.moveTo(440, 370)
				pyautogui.click(button='right')
				pyautogui.moveTo(1037, 599)
				pyautogui.click(button='right')
				pyautogui.moveTo(1061, 416)
				pyautogui.click(clicks=1)
				pyautogui.hotkey('enter')
				pyautogui.moveTo(634, 379)
				pyautogui.click(clicks=1)

				break


