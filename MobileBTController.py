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

        dpg.add_text("Capture Mode", parent="mobile_controller_window")
        dpg.add_group(parent="mobile_controller_window", tag="capture_mode", horizontal=True)
        dpg.add_button(label="Photo Mode", parent="capture_mode", user_data="photo_mode", callback=self.executeCommand)
        dpg.add_button(label="Video Mode", parent="capture_mode", user_data="video_mode", callback=self.executeCommand)
        
        dpg.add_text("Capture Controls", parent="mobile_controller_window")
        dpg.add_group(parent="mobile_controller_window", tag="capture_controls", horizontal=True)
        dpg.add_button(label="Capture", parent="capture_controls", tag="capture_button", user_data="capture", width=100, callback=self.executeCommand)
        dpg.add_button(label="Back", parent="capture_controls", user_data="back", callback=self.executeCommand)
        dpg.bind_item_theme("capture_button", self.theme.captureGreen())

        dpg.add_text("Nav Controls", parent="mobile_controller_window")
        dpg.add_group(parent="mobile_controller_window", tag="nav_controls_top", horizontal=True)
        dpg.add_button(label="Up", parent="nav_controls_top", user_data="nav_up", indent=30, callback=self.executeCommand)
        dpg.add_group(parent="mobile_controller_window", tag="nav_controls_mid", horizontal=True)
        dpg.add_button(label="Left", parent="nav_controls_mid", user_data="nav_left", callback=self.executeCommand)
        dpg.add_button(label="Right", parent="nav_controls_mid", user_data="nav_right", callback=self.executeCommand)
        dpg.add_group(parent="mobile_controller_window", tag="nav_controls_bottom", horizontal=True)
        dpg.add_button(label="Down", parent="nav_controls_bottom", user_data="nav_down", indent=20, callback=self.executeCommand)
        dpg.bind_item_theme("nav_controls_top", self.theme.navBlue())
        dpg.bind_item_theme("nav_controls_mid", self.theme.navBlue())
        dpg.bind_item_theme("nav_controls_bottom", self.theme.navBlue())
