#include <Servo.h>

String coordinates;

Servo pan;
servo tilt;

// attaching servo motors for pan and tilt
void setup() {
  pan.attach(2);
  tilt.attach(3);
  serial.begin(9600);
}


void loop() {
  while(Serial.available())
  {
    coordinates = Serial.readStringUntil('\r');
    Serial.println(coordinates);
    int x_axis = coordinates.substring(0, coordinates.indexOf(',')).toInt();
    int y_axis = coordinates.substring(coordinates.indexOf(',') + 1).toInt();

    // converting from pixel coordinate to servo angle (mapping from resolution to rotation angle)
    int y = map(y_axis, 0, 1080, 180, 0);
    int x = map(x_axis, 0, 1920, 180, 0);

    // moving servos to proper location
    pan.write(x);
    tilt.write(y);
    
    
    Serial.print("First Integer: ");
    Serial.println(x);
    Serial.print("Second Integer: ");
    Serial.println(y);
  }
}