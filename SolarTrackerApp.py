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

