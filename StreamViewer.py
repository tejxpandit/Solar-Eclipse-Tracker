# File : Stream Viewer
# Author : Tej Pandit
# Date : July 2024

import os
import time
import threading
import dearpygui.dearpygui as dpg
import cv2
import numpy as np
from SolarTrackerThemes import SolarTrackerThemes

class StreamViewer:
    def __init__(self):
        self.stream = None
        self.stream_frame = None
        self.serverURL = "192.168.0.105"
        self.streamURL = "http://" + self.serverURL + ":8080/stream.mjpeg"
        self.frame_folder = os.path.join(os.getcwd(), "frames")
        self.frame_file = os.path.join(self.frame_folder, "frame.jpg")
        self.stream_config = {
            "width"     : 0,
            "height"    : 0,
            "channels"  : None,
            "data"      : None,
            "scale"     : 0.6
        }
        self.stream_state = False
        self.stream_thread = None
        self.viewer_thread = None
        self.theme = SolarTrackerThemes()

    # Stream Viewer GUI Controls
    def createStreamViewWindow(self):
        dpg.add_window(label="Solar Eclipse Video Stream", tag="stream_viewer_window")
        dpg.add_button(label="Start Stream", parent="stream_viewer_window", tag="start_stream_button", callback=self.startStream)
        dpg.add_button(label="Stop Stream", parent="stream_viewer_window", tag="stop_stream_button", show=False, callback=self.stopStream) 
        dpg.bind_item_theme("start_stream_button", self.theme.enableGreen())
        dpg.bind_item_theme("stop_stream_button", self.theme.disableRed())

    def startStream(self):
        self.viewer_thread = threading.Thread(target = self.viewerThread)
        self.stream_state = True
        dpg.hide_item("start_stream_button")
        dpg.show_item("stop_stream_button")
        print("Stream Enabled")
        self.viewer_thread.start()

    def stopStream(self):
        self.stream_state = False
        dpg.hide_item("stop_stream_button")
        dpg.show_item("start_stream_button")
        print("Stream Disabled")
        self.viewer_thread.join()

    # Stream Capture
    def streamCapture(self):
        # check, stream_frame = self.stream.read()
        frame = cv2.resize(self.stream_frame,(800,373))
        frame_data = np.flip(frame, 2) # Convert BGR to RGB
        frame_data = frame_data.ravel() # Flatten N-Dim to 1-Dim Structure
        frame_data = np.asarray(frame_data, dtype='f') # Change Data Type to float32
        tex_data = np.true_divide(frame_data, 255.0) # Normalize Texture Data
        self.stream_config["data"] = tex_data

        # print("Frame Array:")
        # print("Array is of type: ", type(frame))
        # print("No. of dimensions: ", frame.ndim)
        # print("Shape of array: ", frame.shape)
        # print("Size of array: ", frame.size)
        # print("Array stores elements of type: ", frame.dtype)

        # self.stream_config["width"] = frame.shape[1]
        # self.stream_config["height"] = frame.shape[0]
        # self.stream_config["channels"] = frame.shape[2]

        # print(self.stream_config["width"])
        # print(self.stream_config["height"])
        # print(self.stream_config["channels"])
        # print(len(self.stream_config["data"]))

        # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # cv2.imshow("Solar Tracker Frame", frame_rgb)
        # cv2.imwrite(self.frame_file, frame)
        # print("stream data captured")

    # Stream Thread
    def streamThread(self):
        while self.stream_state:
            try:
                check, self.stream_frame = self.stream.read()
            except:
                print("Failed to Capture Stream @ " + self.streamURL)
            time.sleep(0.01)

    # Viewer Thread
    def viewerThread(self):
        self.stream = cv2.VideoCapture(self.streamURL)
        self.stream_thread = threading.Thread(target = self.streamThread)
        self.stream_thread.start()
        time.sleep(2)
        while self.stream_state:
            self.streamCapture()
            self.updateFrame()
            time.sleep(0.2)
        self.stream_thread.join()
        self.stream.release()

    def updateFrame(self):
        # Load New Image (width and height should match!)
        # self.stream_config["width"], self.stream_config["height"], self.stream_config["channels"], self.stream_config["data"] = dpg.load_image(self.frame_file)
        # Update Image
        dpg.set_value("stream_tex", self.stream_config["data"])
        # print("frame updated")

    def initializeStreamFrame(self):
        # Set Initial Stream Frame
        dpg.add_image(texture_tag="stream_tex", parent="stream_viewer_window", tag="stream_frame", width=self.stream_config["width"]*self.stream_config["scale"], height=self.stream_config["height"]*self.stream_config["scale"])
        