# File : Test : Mobile Phone Webcam Server
# Author : Tej Pandit
# Date : April 2024
# NOTE : Tested with Android App [ScreenStream by Dmytro Kryvoruchko]

import torch
import cv2
from time import sleep

URL = "http://" + "192.168.0.105" + ":8080/stream.mjpeg"


key = cv2. waitKey(1)
webcam = cv2.VideoCapture(URL)
#webcam = cv2.VideoCapture(0)
sleep(2)

frame_number = 0
while True:

    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
 
        if(frame_number > 1):
            img = cv2.resize(frame,(640,480))
            #cv2.imshow("Img", img)

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # results = model(img_rgb)

            
            cv2.imshow("YOLO", img)
            #print(results)

            
            frame_number = 0
        else:
            frame_number += 1

        
        #results.show()

        key = cv2.waitKey(1)
        if key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
    
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

