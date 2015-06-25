#include <Servo.h> 

Servo servo;

int base = 90;
int arm = 90;
int forearm = 90;
int gripper = 25;

void setup() 
{ 
  //  pinMode(led, OUTPUT);     
  Serial.begin(9600);
  servo.attach(6);
} 

void loop() 
{ 
  if(Serial.available()){
    // char inByte = Serial.read();
    // int temp = Serial.read();
    int baseTemp = Serial.parseInt();
    int armTemp = Serial.parseInt();
    int forearmTemp = Serial.parseInt();
    int gripperTemp = Serial.parseInt();
    if (baseTemp > 0)
      base = baseTemp;
    if (armTemp > 0)
      arm = armTemp;
    if (forearmTemp > 0)
      forearm = forearmTemp;
    if (gripperTemp > 0)
      gripper = gripperTemp;
    String comma = ", ";
    String total = base + comma + arm + comma + forearm + comma + gripper;
    Serial.println(total);
  }
  
  servo.write(gripper);
  // delay(15);

}

