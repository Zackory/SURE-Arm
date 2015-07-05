#include <Servo.h>

Servo baseServo;
Servo armServo;
Servo forearmServo;
Servo gripperServo;

int base = 90;
int arm = 90;
int forearm = 90;
int gripper = 25;

int leftMotorPin = 5;
int rightMotorPin = 9;
int leftMotor = 0;
int leftMotor_Cont_1= 2;
int rightMotor_Cont_1= 4;
int rightMotor = 0;

void setup()
{
    Serial.begin(9600);
    baseServo.attach(3);
    armServo.attach(6);
    forearmServo.attach(10);
    gripperServo.attach(11);
    pinMode(leftMotorPin, OUTPUT);
    pinMode(leftMotor_Cont_1, OUTPUT);
    pinMode(leftMotor_Cont_2, OUTPUT);
    pinMode(rightMotorPin, OUTPUT);
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
        int leftMotorTemp = Serial.parseInt();
        int rightMotorTemp = Serial.parseInt();
        if (baseTemp > 0)
            base = baseTemp;
        if (armTemp > 0)
            arm = armTemp;
        if (forearmTemp > 0)
            forearm = forearmTemp;
        if (gripperTemp > 0)
            gripper = gripperTemp;
        if (leftMotorTemp > 0)
            leftMotor = leftMotorTemp;
            digitalWrite(leftMotor_Cont_1, HIGH);
            digitalWrite(leftMotor_Cont_2, LOW);
        if (leftMotor> 255)
            leftMotor = 255;
        if (rightMotorTemp > 0)
            rightMotor = rightMotorTemp;
        String comma = ", ";
        String total = base + comma + arm + comma + forearm + comma + gripper + comma + leftMotor + comma + rightMotor;
        Serial.println(total);
    }

    baseServo.write(base);
    armServo.write(arm);
    forearmServo.write(forearm);
    gripperServo.write(gripper);
    // delay(15);

    // Write to drive motors
    analogWrite(leftMotorPin, leftMotor);
    analogWrite(rightMotorPin, rightMotor);
}

