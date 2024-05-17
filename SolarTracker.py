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

    def setDateTime(self):
        self.date_time = datetime.now(tz=ZoneInfo("America/Chicago"))
        # self.date_time = datetime(2024, 4, 4, 18, 0, 0, 0, tzinfo=ZoneInfo("America/Chicago"))


    # TEST : GENERATE SOLAR ECLIPSE ROUTINE
    def generateDayRoutine(self):
        self.day_routine = []
        for h in range(8, 18, 1): # hours
            for m in range(0, 60, 10): # minutes
                self.day_routine.append(datetime(2024, 4, 4, h, m, 0, 0, tzinfo=ZoneInfo("America/Chicago")))

    