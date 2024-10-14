# Face Tracking with OpenCV, Arduino, and Servo Motors

This project utilizes OpenCV for face detection and Arduino with servo motors to track the detected face in real-time. The program uses a webcam to capture video, detect faces, and control two servo motors (pan and tilt) to follow the detected face.

## Project Overview

This project consists of two main parts:
1. **Python Script**: Uses OpenCV to detect faces through a webcam and sends face coordinates via serial communication to the Arduino.
2. **Arduino Code**: Receives face coordinates, maps them to servo angles, and moves the servo motors accordingly to track the face.

## Hardware Requirements

- Arduino (e.g., Arduino Uno)
- 2 Servo Motors (Pan and Tilt)
- Webcam
- Jumper Wires
- Breadboard
- USB cable for Arduino


## Setup Instructions

### 1. Arduino Setup

1. **Connect the Servos**:
    - Connect the Pan servo to pin 2 on the Arduino.
    - Connect the Tilt servo to pin 3 on the Arduino.

2. **Upload the Arduino Code**:
    - Open the Arduino IDE.
    - Copy the provided Arduino code into the editor.
    - Upload the code to your Arduino board.

### 2. Python Script

1. **Install Dependencies**:
   Install the required Python libraries using the following command:

   ```shell
   pip install opencv-python pyserial numpy
   ```
   
2. **Run the Script**
   Run this command to run the script while the Arduino is connected to the computer:
   
   ```shell
   python3 face_detection.py
   ```
