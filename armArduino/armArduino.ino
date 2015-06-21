#include <Servo.h> 

Servo servo;

int angle = 0;

void setup() 
{ 
  //  pinMode(led, OUTPUT);     
  Serial.begin(9600);
  servo.attach(6);
} 

void loop() 
{ 
  if(Serial.available()){ // only send data back if data has been sent
    // char inByte = Serial.read(); // read the incoming data
    int temp = Serial.parseInt();
    if (temp >= 0) {
      angle = temp;
      Serial.println(angle); // send the data back in a new line so that it is not all one long line
    }
  }
  
  servo.write(angle);
  // delay(15);

}

