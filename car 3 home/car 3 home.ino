/*obstacle avoiding, Bluetooth control, voice control robot car.
   https://srituhobby.com
*/
//#include <iostream>
using namespace std;
#include <String.h>
#include <Servo.h>
#include <AFMotor.h>
#define Echo A0
#define Trig A1
#define motor 10
#define Speed 250
#define spoint 103
int j=1; 
char value;
int distance;
int Left;
int Right;
int L = 0;
int R = 0;
int L1 = 0;
int R1 = 0;
int a=1;
Servo servo;
AF_DCMotor M1(1);
AF_DCMotor M2(2);
AF_DCMotor M3(3);
AF_DCMotor M4(4);
void setup() {
  Serial.begin(9600);
  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);
  servo.attach(motor);
  M1.setSpeed(Speed);
  M2.setSpeed(Speed);
  M3.setSpeed(Speed);
  M4.setSpeed(Speed);
}
void loop() 
{
  a=0;
    if (Serial.available() > 0) {
      value = Serial.read();
      Serial.println(value);
      a=value;
    if (a == '1') {
      Serial.println("obstacle");
      Obstacle();
  } else if (a == '2') {
    Serial.println("bt control");
    Bluetoothcontrol();
  } else if (a == '3') {
    Serial.println("voice control");
    voicecontrol();
  }
}
}
void Bluetoothcontrol() {
 Serial.println("bt cont initi"); 
 j=0;
    if (Serial.available() > 0) {
      value = Serial.read();
      Serial.println(value);
      j=value;
    if (j == 'F') 
    { 
      Serial.println("forward work");
      forward();
    } 
    else if (value == 'B') 
    {
      backward();
    } 
    else if (value == 'L') 
    {
      left();
    } 
    else if (value == 'R') 
    {
      right();
    }
    else if (value== 'S') 
    {
      Stop();
    } 
    else if (value == 'G')
    {
      topleft();
    } 
    else if (value== 'I')
    {
      topright();
    } 
    else if (value== 'H')
    {
      bottomleft();
    } 
    else if (value== 'J')
    {
      bottomleft();
    }
  }  
}
void Obstacle() {
  Serial.println("obstacle initi");
  distance = ultrasonic();
  if (distance <= 12) {
    Stop();
    backward();
    delay(100);
    Stop();
    L = leftsee();
    servo.write(spoint);
    delay(800);
    R = rightsee();
    servo.write(spoint);
    if (L < R) {
      right();
      delay(500);
      Stop();
      delay(200);
    } else if (L > R) {
      left();
      delay(500);
      Stop();
      delay(200);
    }
  } else {
    forward();
  }
}
void voicecontrol() {
  Serial.println("voice cont initi"); 
  if (Serial.available() > 0) {
    value = Serial.read();
    Serial.println(value);
    if (value == '^') {
      Serial.println("forward work");
      forward();
    } else if (value == '-') {
      backward();
    } else if (value == '<') {
      L = leftsee();
      servo.write(spoint);
      if (L >= 10 ) {
        left();
        delay(500);
        Stop();
      } else if (L < 10) {
        Stop();
      }
    } else if (value == '>') {
      R = rightsee();
      servo.write(spoint);
      if (R >= 10 ) {
        right();
        delay(500);
        Stop();
      } else if (R < 10) {
        Stop();
      }
    } else if (value == '*') {
      Stop();
    }
  }
}
// Ultrasonic sensor distance reading function
int ultrasonic() {
  Serial.println("obstacle in");
  digitalWrite(Trig, LOW);
  delayMicroseconds(4);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);
  long t = pulseIn(Echo, HIGH);
  long cm = t / 29 / 2; //time convert distance
  return cm;
}
void forward() {
  Serial.println("forward in");
  M1.run(FORWARD);
  M2.run(FORWARD);
  M3.run(FORWARD);
  M4.run(FORWARD);
  delay(1000);
}
void backward() {
  M1.run(BACKWARD);
  M2.run(BACKWARD);
  M3.run(BACKWARD);
  M4.run(BACKWARD); 
  delay(1000);
}
void right() {
  M1.run(BACKWARD);
  M2.run(BACKWARD);
  M3.run(FORWARD);
  M4.run(FORWARD); 
  delay(1000);
}
void left() {
  M1.run(FORWARD);
  M2.run(FORWARD);
  M3.run(BACKWARD);
  M4.run(BACKWARD); 
  delay(1000);
}
void Stop() {
  M1.run(RELEASE);
  M2.run(RELEASE);
  M3.run(RELEASE);
  M4.run(RELEASE); delay(1000);
}
void topleft(){
  M1.setSpeed(Speed); //Define maximum velocity
  M1.run(FORWARD); //rotate the motor clockwise
  M2.setSpeed(Speed); //Define maximum velocity
  M2.run(FORWARD); //rotate the motor clockwise
  M3.setSpeed(Speed/3.1);//Define maximum velocity
  M3.run(FORWARD); //rotate the motor clockwise
  M4.setSpeed(Speed/3.1);//Define maximum velocity
  M4.run(FORWARD); //rotate the motor clockwise
}
void topright()
{
  M1.setSpeed(Speed/3.1); //Define maximum velocity
  M1.run(FORWARD); //rotate the motor clockwise
  M2.setSpeed(Speed/3.1); //Define maximum velocity
  M2.run(FORWARD); //rotate the motor clockwise
  M3.setSpeed(Speed);//Define maximum velocity
  M3.run(FORWARD); //rotate the motor clockwise
  M4.setSpeed(Speed);//Define maximum velocity
  M4.run(FORWARD); //rotate the motor clockwise
}
void bottomleft()
{
  M1.setSpeed(Speed); //Define maximum velocity
  M1.run(BACKWARD); //rotate the motor anti-clockwise
  M2.setSpeed(Speed); //Define maximum velocity
  M2.run(BACKWARD); //rotate the motor anti-clockwise
  M3.setSpeed(Speed/3.1); //Define maximum velocity
  M3.run(BACKWARD); //rotate the motor anti-clockwise
  M4.setSpeed(Speed/3.1); //Define maximum velocity
  M4.run(BACKWARD); //rotate the motor anti-clockwise
}
void bottomright()
{
  M1.setSpeed(Speed/3.1); //Define maximum velocity
  M1.run(BACKWARD); //rotate the motor anti-clockwise
  M2.setSpeed(Speed/3.1); //Define maximum velocity
  M2.run(BACKWARD); //rotate the motor anti-clockwise
  M3.setSpeed(Speed); //Define maximum velocity
  M3.run(BACKWARD); //rotate the motor anti-clockwise
  M4.setSpeed(Speed); //Define maximum velocity
  M4.run(BACKWARD); //rotate the motor anti-clockwise
}
int rightsee() {
  servo.write(20);
  delay(800);
  Left = ultrasonic();
  return Left;
}
int leftsee() {
  servo.write(180);
  delay(800);
  Right = ultrasonic();
  return Right;
}