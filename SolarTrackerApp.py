# File : Solar Tracker App
# Author : Tej Pandit
# Date : April 2024

import dearpygui.dearpygui as dpg
from TurretController import TurretController
from DynamixelTurret import DynamixelTurret
from SolarTracker import SolarTracker
from StreamViewer import StreamViewer
from MobileBTController import MobileBTController

# DPG Context
dpg.create_context()
dpg.configure_app(init_file="solartracker.ini")

# DPG Viewport
dpg.create_viewport(title="Solar Eclipse Tracker", width=1100, height=650, small_icon="SolarEclipse.ico", large_icon="SolarEclipse.ico")
dpg.set_exit_callback(lambda: dpg.save_init_file("solartracker.ini"))

# Solar Tracker
tracker = SolarTracker()

# Dynamixel Turret
dmx = DynamixelTurret()

# Turret Controller
turret = TurretController()
turret.dmx = dmx
turret.tracker = tracker
turret.createTurretControllerWindow()

# DPG Render Context
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()