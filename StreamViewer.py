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

