# File : Turret Controller
# Author : Tej Pandit
# Date : April 2024

import time
import dearpygui.dearpygui as dpg
import threading
from SolarTrackerThemes import SolarTrackerThemes

class TurretController:
    def __init__(self):
        self.varName = None
        self.turretState = False
        self.dmx = None
        self.tracker = None
        self.turretThread = None
        self.theme = SolarTrackerThemes()

        # Callibration Offsets
        self.rotate_offset = 0
        self.tilt_offset = 90

        # Error Correction Offsets
        self.rotate_error_correction = 0
        self.tilt_error_correction = 0

    def createTurretControllerWindow(self):
        dpg.add_window(label="Turret Controls", tag="turret_control_window")
        dpg.add_button(label="Start Tracker", parent="turret_control_window", tag="start_tracking_button", callback=self.startTracker)
        dpg.add_button(label="Stop Tracker", parent="turret_control_window", tag="stop_tracking_button", show=False, callback=self.stopTracker) 
        dpg.bind_item_theme("start_tracking_button", self.theme.enableGreen())
        dpg.bind_item_theme("stop_tracking_button", self.theme.disableRed())