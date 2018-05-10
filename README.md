# Audio Arm 
#### Robert Jomar Malate 
#### Freshman Seminar 50F: Artificial and Natural Intelligence 

## Introduction 
This project explores the capabilities of speech recognition with its application to robotics.  By speaking to the computer particular key phrases, a servo will move in response, which in turn moves the robot arm. 

## Files 

The code for the servo control and speech recognition could be found at the following GitHub link:
https://github.com/RobJMal/Audio_Arm 


## How it works 

The software can be broken down to two parts: speech recognition/processing and servo control. 
### Speech Recognition/Processing
Using Python and its available libraries, I created a program that took in a command through the microphone, validated the command, and send the proper response to the Arduino. Because of the simplicity and wide availability of libraries, Python was used as the backbone of the project to carry out these tasks. 

First, the program opens up access to the Arduino by setting up the COM port and baud rate.  Then, it accesses the microphone.  When the program is run, it begins listening for five seconds for voice commands.  After recieving the input, it is then run through a condition that checks if the input is inside the command-word list.  If so, it sends the Arduino the proper signal using numbers ```1, 2, or 3```. 

Code can be found in ```voice_armcontrol.py```. 

### Servo Control 
Using the Arduino Uno microcontroller, I was able to take in the signal from Python program and output a servo movement.  Arduino made it easy to interact with the servo, thus making it the optimal choice for servo control.  

After going though the initial set up phases, the conditional then checks the Serial input that is has received from the Python program.  If it is a ```1```, it moves the servo left; if it is a ```2```, it moves the servo right; if it is a ```3```, it moves the servo towards the center position.  

Code can be found in ```voice_armcontrol/voice_armcontrol.ino```. 

### Commands 
The program takes in the following commands:

- Moving left: 
	- "left"
	- "Obama"
	- "liberal"
- Moving right
	- "right"
	- "Trump"
	- "conservative"
- Moving to center position 
	- "center" 

## Interesting Notes 

While the code may look simple, the speech recognition that is being done is quite sophisticated. 


## Bibliography/Resources
Although none of the tutorials below explicitly gave instructions on how to control a servo via voice commands, each one gave me guidance on particular components of the project that when synthesized, created the final product. 

- Python to Arduino Communication: http://www.instructables.com/id/Arduino-and-Python/ 
- Speech Recogntion: https://realpython.com/python-speech-recognition/
- Servo control: https://www.arduino.cc/en/Reference/Servo 


