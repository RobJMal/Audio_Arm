import serial
import speech_recognition as sr 
import pyaudio

# Object in Recognizer class
r = sr.Recognizer() 

# Opens Arduino to recieve commands 
arduino = serial.Serial("COM3", 9600)

# Object in Microphone class 
mic = sr.Microphone() 

# Signals to send to arduino 
left_signal = "1"
right_signal = "2"
center_signal = "3"

# Command words for moving arm 
left_commands = ["left", "Obama", "liberal"]
right_commands = ["right", "Trump", "conservative"]
center_commands = ["center", "Center"]

# Takes in input from microphone 
with mic as source: 
	r.adjust_for_ambient_noise(source)
	print("Say command: ")
	audio = r.listen(source, 5)
	print("Stop")

input_cmd = r.recognize_google(audio)

# Checks commands and sends output to Arduino 
if (input_cmd in left_commands):
	arduino.write("1")
elif (input_cmd in right_commands):
	arduino.write("2")
elif (input_cmd in center_commands):
	arduino.write("3")

print(input_cmd)


