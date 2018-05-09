#include <Servo.h>

Servo myServo; 

// Stores position of servo 
int pos = 90; 

void setup() {
  Serial.begin(9600);    
  myServo.attach(9); 
  myServo.write(pos); 
}

void loop() {
  
  // Moves servo left 
  if(Serial.available() == 1) {
    pos -= 30; 
    myServo.write(pos);
    delay(100); 
  }

  // Moves servo right 
  if(Serial.available() == 2) {
    pos += 30; 
    myServo.write(0); 
    delay(100); 
  }

  // Moves servo center position  
  if(Serial.available() == 3) {
    pos = 90; 
    myServo.write(pos); 
    delay(100); 
  }

}
