"""
 __________________________________________________________                                                
|  RRRRR                         PPPPP                     |
|  R    R                        P    P   ii               |
|  R     R   aaaaa      ssssss   P     P       n nnnnnn    |   
|  R    R   a     a    s         P    p   ii   nn      nn  |
|  RRRRR   a       a    ssssss   PPPPP    ii   n        n  |    
|  R    R   a     aa          s  P        ii   n        n  |
|  R     R   aaaaa aa   ssssss   P        ii   n        n  |
|__________________________________________________________|
|                                                          |
|         All Rights Reserved © 2017 SaeedEY.com           |
|  RasPin is an Open Source Script to Provide You an Easy  |
|  Access to your RaspberryPi Pins Just to send out Power  |
|  from Specified Pin.                                     |
|                                                          |
|  details:                                                |
|          Version: 1                                      |
|          Last Modify: 11/April/2017                      |
|  Find Me@:                                               |
|          https://SaeedEY.com                             |
|          https://github.com/SaeedEY                      |
|  USAGE:                                                  |
|          python Pins [PinNumber] on/off/r [sleep/s]      |
|  ValidPinsNumber:                                        |
|        [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26]  |
|__________________________________________________________|

"""
import RPi.GPIO as GPIO
import sys
import os
import signal
import glob

from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pinArrays = {3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26}
curPin = []
dirs = './Pins'

def checkPins():
	global dirs 
	if not os.path.exists(dirs):
		os.makedirs(dirs)
	global curPin
	tmp = []
	tmp = os.listdir(dirs)
	for x in tmp:
		curPin.append(int(x.split('.p')[0]))
	return curPin
curPin = checkPins()
print(curPin)
def onStop(var):
	global dirs
	if(var is not None):
		if(var == 0):
			for x in curPin:
				x = int(x)
				Todo(x,'off',0)
				os.rmdir(dirs+'/'+str(x)+'.pin')
		else:
			GPIO.setup(var,GPIO.OUT)
			GPIO.output(var,0)
	print('\n Program Stopped')
	try:
		for x in curPin:
			if(GPIO.input(x)==True):
				GPIO.output(x,0)
		GPIO.cleanup()
		print('\n Program Stopped')
		#sys.exit(0)

	except KeyboardInterrupt:
		
		GPIO.cleanup()
		print('\n Program Stopped')
		#sys.exit(0)

def Todo(port,action,slep):
	global curPin
	global dirs
###		sys.exit()
###	print("port "+str(port)+" with "+str(slep)+" time action "+str(action))
	if(type(port) is int and port !=0):
###		print("Unknown Port.")
		GPIO.setup(port, GPIO.OUT)
	if(type(port) is not int):
		print('')
	if(type(slep) is not int):
###		print("Sleep Time set to 1")
		slep = 1
	if(action == "off" or action == 0):
		curPin = checkPins()
		if(port == 0):
			for x in curPin:
				GPIO.setup(x,GPIO.OUT)
				if(GPIO.input(x)==True):
					GPIO.output(x,GPIO.LOW)
					os.rmdir(dirs+'/'+str(x)+'.pin')
		else:
			sleep(slep)
###             	print("Stopped")
			os.rmdir(dirs+'/'+str(port)+'.pin')
			GPIO.output(port, GPIO.LOW)
	elif(action == "on" or action == 1):
		if(port == 0):
			for x in pinArrays:
				GPIO.setup(x,GPIO.OUT)
				if(GPIO.input(x)==False):
					GPIO.output(x,GPIO.HIGH)
					os.makedirs(dirs+'/'+str(x)+'.pin')

		else:
			sleep(slep)
###             	print("Started")
			os.makedirs(dirs+'/'+str(port)+'.pin')
			GPIO.output(port,GPIO.HIGH)
	if(port == 0):
		return False
	else:
		return GPIO.input(port)

def signal_handler(signal, frame):
	onStop('')
def stopListener():
	signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
	po = 0
	ac = 'off'
	sl = 0
	if len(sys.argv) == 4 :
		if sys.argv[1] is not None :        
			po = int(sys.argv[1])
		if sys.argv[2] is not None :
			ac = str(sys.argv[2])
		if sys.argv[3] is not None :
			sl = int(sys.argv[3])
		if(ac == 'r'):
			Todo(0,'on',0)
			Todo(0,'off',0)
			sys.exit()
	else:
		po  = input('Please Enter Pin :>')
		ac  = raw_input('Please Enter Action (on/1 & off/2) :>')
		sl  = input('Please Enter Sleep (x Second) :>')
		if(ac == str(1)):
                        ac = 'on'
		if(ac == str(2)):
                        ac = 'off'
	Todo(int(po) , str(str.lower(ac)) ,int(sl))
