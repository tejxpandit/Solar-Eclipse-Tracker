# File : Dynamixel Turret
# Author : Tej Pandit
# Date : April 2024

import os
from dynamixel_sdk import *

class DynamixelTurret:
    def __init__(self):
        self.DEVICENAME = 'COM3'
        self.PROTOCOL_VERSION = 2.0
        self.BAUDRATE = 1000000

        self.servos =   {   "rotate" : { 
                                "id" : 1,
                                "range_min" : 0,
                                "range_max" : 3070,
                                "angle" : 1500
                            },

                            "tilt" : { 
                                "id" : 2,
                                "range_min" : 1000,
                                "range_max" : 3070,
                                "angle" : 1500
                            }
                        }
        self.servo_angle_max_degree = 360
        self.servo_angle_max_dynamix = 4096

        if os.name == 'nt':
            import msvcrt
            def getch():
                return msvcrt.getch().decode()
