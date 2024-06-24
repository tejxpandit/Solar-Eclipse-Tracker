# File : Mobile Bluetooth Controller
# Author : Tej Pandit
# Date : April 2024

import time
import dearpygui.dearpygui as dpg
import serial
from SolarTrackerThemes import SolarTrackerThemes

class MobileBTController:
    def __init__(self):
        self.bt_com = None # Bluetooth COM Port
        self.bt_com_port = "COM7"
        self.bt_com_baud = 9600
        self.bt_com_timeout = 5
        self.bt_state = False
        self.command = ""
        self.theme = SolarTrackerThemes()
