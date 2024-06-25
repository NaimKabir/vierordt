import serial 
import time 
arduino = serial.Serial(port='/dev/cu.usbmodem2101', baudrate=115200, timeout=.1) 
def read(): 
	   data = arduino.readline() 
	   return data 

while True: 
	   time.sleep(0.05) 
	   value = read() 
	   print(value) # printing the value 
