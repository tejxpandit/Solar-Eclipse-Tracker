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