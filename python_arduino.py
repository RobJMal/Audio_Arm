import serial 

connected = False 

arduino = serial.Serial("COM3", 9600)

while not connected: 
	arduino_in = arduino.read() 
	connected = True 

arduino.write("1")

while arduino.read () == '1':
	arduino.read()

arduino.close() 
