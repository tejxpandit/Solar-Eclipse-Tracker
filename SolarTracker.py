# File : Solar Tracker with Servo Turret
# Author : Tej Pandit
# Date : April 2024

import pysolar.solar as sol
from datetime import datetime
from zoneinfo import ZoneInfo

class SolarTracker:
    def __init__(self):
        self.latitude = 29.5203
        self.longitude = -98.6017
        self.date_time = None
        self.day_routine = None

