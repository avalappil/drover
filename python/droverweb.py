import webiopi
import os,time

nfaces = "0"

# import Serial driver
from webiopi.devices.serial import Serial

# initialize Serial driver
serial = Serial("ttyAMA0", 9600)
def setup():
    # empty input buffer before starting processing
    while (serial.available() > 0):
        serial.readstrDataing()

@webiopi.macro
def setfaces(aData):
    global nfaces
    nfaces = aData

@webiopi.macro
def numoffaces(aData):
    global nfaces
    return nfaces

@webiopi.macro
def loadData(strData):
    print (strData)
    if (strData == "1"):
    	serial.write(bytes("Leftforward\r\n", 'UTF-8'))
    elif (strData == "2"):
    	serial.write(bytes("forward\r\n", 'UTF-8'))
    elif (strData == "3"):
    	serial.write(bytes("Rightforward\r\n", 'UTF-8'))
    elif (strData == "4"):
    	serial.write(bytes("Rotateleft\r\n", 'UTF-8'))
    elif (strData == "5"):
    	serial.write(bytes("Stop\r\n", 'UTF-8'))
    elif (strData == "6"):
    	serial.write(bytes("Rotateright\r\n", 'UTF-8'))
    elif (strData == "7"):
    	serial.write(bytes("LeftReverse\r\n", 'UTF-8'))
    elif (strData == "8"):
    	serial.write(bytes("Reverse\r\n", 'UTF-8'))
    elif (strData == "9"):
    	serial.write(bytes("RightReverse\r\n", 'UTF-8'))
    elif (strData != "" and strData.startswith('l')):        
        headPos = strData.split('@')
        data = "#15 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))
    elif (strData != "" and strData.startswith('r')):
        headPos = strData.split('@')
        data = "#15 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))
    elif (strData != "" and strData.startswith('t')):
        headPos = strData.split('@')
        data = "#31 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))
    #elif (strData == "x"):
    #elif (strData == "y"):