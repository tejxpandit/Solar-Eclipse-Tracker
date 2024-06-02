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

        MY_DXL = 'X_SERIES'
        if MY_DXL == 'X_SERIES' or MY_DXL == 'MX_SERIES':
            self.ADDR_TORQUE_ENABLE          = 64
            self.ADDR_GOAL_POSITION          = 116
            self.ADDR_PRESENT_POSITION       = 132
        self.TORQUE_ENABLE               = 1     # Value for enabling the torque
        self.TORQUE_DISABLE              = 0     # Value for disabling the torque
        self.DXL_MOVING_STATUS_THRESHOLD = 20    # Dynamixel moving status threshold

        self.initController()
        self.initServos()

    def initController(self):
        try:
            self.portHandler = PortHandler(self.DEVICENAME)
            self.packetHandler = PacketHandler(self.PROTOCOL_VERSION)
        except:
            print("No Turret Detected on " + str(self.DEVICENAME))
            exit(1)

    def initServos(self):
        for name, details in self.servos.items():
            self.initServo(name)

    def initServo(self, name):
        id = self.servos[name]["id"]
        try:
            self.portHandler.openPort()
            self.portHandler.setBaudRate(self.BAUDRATE)
            # Enable Dynamixel Torque
            dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, id, self.ADDR_TORQUE_ENABLE, self.TORQUE_ENABLE)
            if dxl_comm_result == COMM_SUCCESS:
                print("Connected to Dynamixel Servo : " + name + ", ID : " + str(id))
            else:
                print(self.packetHandler.getTxRxResult(dxl_comm_result), self.packetHandler.getRxPacketError(dxl_error))
        except:
            print("Failed to Connect Servo : " + name + ", ID : " + str(id))