import serial
import time
import numpy as np
import cv2

arduinoData = serial.Serial('/dev/tty.usbmodem101', 9600) #Change this based on your serial port

def send_coordinates_to_arduino(x, y, w, h):
    # Convert the coordinates to a string and send it to Arduino
    coordinates = f"{x},{y}\r"
    arduinoData.write(coordinates.encode())
    # Printing coordinates
    print(f"{x = }Y{y = }\n")

# Capturing video using default camera
capture = cv2.VideoCapture(0)  

# Loading OpenCV model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    # Capturing video stream frame by frame
    isTrue, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 8, minSize=(120,120)) # Detecting faces in each frame and receiving coordinates

    # Retrieving only one face (in case of multiple detections)
    x, y, w, h = faces[0]
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5) # Drawing rectangle around the detected face
    send_coordinates_to_arduino(x, y, w, h) # Sending coordinates through serial to Arduino

    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv2.destroyAllWindows()
