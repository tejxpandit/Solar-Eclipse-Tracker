# File : Test : Mobile Phone Webcam Server
# Author : Tej Pandit
# Date : April 2024
# NOTE : Tested with Android App [ScreenStream by Dmytro Kryvoruchko]

import torch
import cv2
from time import sleep

URL = "http://" + "192.168.0.105" + ":8080/stream.mjpeg"

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5m')  # Default Device GPU
#model = torch.hub.load('ultralytics/yolov5', 'yolov5m', device="cpu") # Run with CPU

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(URL)
#webcam = cv2.VideoCapture(0)
sleep(2)

frame_number = 0
while True:

    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
 
        
    
    except(KeyboardInterrupt):
        print("Turning off camera.")
        

