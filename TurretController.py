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

        # Error Correction Controls
        dpg.add_text("Error Correction", parent="turret_control_window")
        dpg.add_slider_float(label="Rotate Error", parent="turret_control_window", tag="rotate_error_slider", min_value=-20, max_value=+20, default_value=0, callback=None)
        dpg.add_slider_float(label="Tilt Error", parent="turret_control_window", tag="tilt_error_slider", min_value=-20, max_value=+20, default_value=0, callback=None)

        # Fine Error Correction Controls
        dpg.add_text("Error Finetuning", parent="turret_control_window")
        dpg.add_slider_float(label="Rotate Error Fine", parent="turret_control_window", tag="rotate_error_fine_slider", min_value=-2, max_value=+2, default_value=0, callback=None)
        dpg.add_slider_float(label="Tilt Error Fine", parent="turret_control_window", tag="tilt_error_fine_slider", min_value=-2, max_value=+2, default_value=0, callback=None)

        # TEST : Manual Callibration Controls
        # dpg.add_slider_int(label="Rotate", parent="turret_control_window", tag="rotate_slider", min_value=0, max_value=360, default_value=180, callback=None)
        # dpg.add_slider_int(label="Tilt", parent="turret_control_window", tag="tilt_slider", min_value=0, max_value=360, default_value=90, callback=None)

        # TEST : Solar Daily Routine
        dpg.add_button(label="Day Routine", parent="turret_control_window", tag="day_routine_button", callback=self.solarTrackerRoutine)

    