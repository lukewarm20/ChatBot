import os
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
                        if "PING" in line:
                                s.send(line.replace("PING", "PONG"))
                                break
                        user = getUser(line)
                        message = getMessage(line)
                        print user + " typed :" + message
			cmd="echo "+message
			os.system(cmd)
                        ##if "" in message:

                                ##os.system("'message'")
                                ##sendMessage(s, message + " extra text afterwards, no harm!")
                                ##break
