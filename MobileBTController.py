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

    # BT Controller Window
    def createBTControllerWindow(self):
        dpg.add_window(label="Mobile Camera Bluetooth Controller", tag="mobile_controller_window")
        dpg.add_button(label="Connect BT", parent="mobile_controller_window", tag="start_bt_button", callback=self.startBTCom)
        dpg.add_button(label="Disconnect BT", parent="mobile_controller_window", tag="stop_bt_button", show=False, callback=self.stopBTCom) 
        dpg.bind_item_theme("start_bt_button", self.theme.enableGreen())
        dpg.bind_item_theme("stop_bt_button", self.theme.disableRed())
