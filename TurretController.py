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

