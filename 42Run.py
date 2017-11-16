import os
import time
import pyautogui
import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			print(line)
                        user = getUser(line)
                        message = getMessage(line)
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
                        if "!" in message:
                                pyautogui.hotkey('enter')
                                break
