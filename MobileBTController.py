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

        dpg.add_text("Zoom Controls", parent="mobile_controller_window")
        dpg.add_group(parent="mobile_controller_window", tag="zoom_controls", horizontal=True)
        dpg.add_button(label="Zoom +", parent="zoom_controls", user_data="zoom_in", callback=self.executeCommand)
        dpg.add_button(label="Zoom -", parent="zoom_controls", user_data="zoom_out", callback=self.executeCommand)

        dpg.add_text("Zoom In Shortcuts", parent="mobile_controller_window")
        dpg.add_group(parent="mobile_controller_window", tag="zoom_in_shortcuts", horizontal=True)
        dpg.add_button(label="Zoom x1", parent="zoom_in_shortcuts", user_data="zoom_x1", callback=self.executeCommand)
        dpg.add_button(label="Zoom x10", parent="zoom_in_shortcuts", user_data="zoom_x10", callback=self.executeCommand)
        dpg.add_button(label="Zoom x50", parent="zoom_in_shortcuts", user_data="zoom_x50", callback=self.executeCommand)
        dpg.add_button(label="Zoom x100", parent="zoom_in_shortcuts", user_data="zoom_x100", callback=self.executeCommand)

        dpg.add_text("Zoom Out Shortcuts", parent="mobile_controller_window")
        dpg.add_group(parent="mobile_controller_window", tag="zoom_out_shortcuts", horizontal=True)
        dpg.add_button(label="Zoom -x1", parent="zoom_out_shortcuts", user_data="zoom_mx1", callback=self.executeCommand)
        dpg.add_button(label="Zoom -x10", parent="zoom_out_shortcuts", user_data="zoom_mx10", callback=self.executeCommand)
        dpg.add_button(label="Zoom -x50", parent="zoom_out_shortcuts", user_data="zoom_mx50", callback=self.executeCommand)
        dpg.add_button(label="Zoom -x100", parent="zoom_out_shortcuts", user_data="zoom_mx100", callback=self.executeCommand)

    def startBTCom(self):
        dpg.hide_item("start_bt_button")
        dpg.show_item("stop_bt_button")
        print("Connecting to BT")
        self.connectBT()

    def stopBTCom(self):
        dpg.hide_item("stop_bt_button")
        dpg.show_item("start_bt_button")
        print("Disconnecting from BT")
        self.disconnectBT()

    # Bluetooth Connection and Transmission Functions
    def connectBT(self):
        try:
            self.bt_com = serial.Serial(self.bt_com_port, self.bt_com_baud, timeout=self.bt_com_timeout)
            print("BT Device Connected!")
            self.bt_state = True
            time.sleep(1)
        except:
            print("Unable to Connect to BT Device!")
            self.bt_state = False
            self.stopBTCom()

    def disconnectBT(self):
        if self.bt_state:
            # serial.Serial.reset_output_buffer() # OPTIONAL BUFFER FLUSH
            self.bt_com.close()
            self.bt_state = False

    def sendCommandBT(self, command):
        if self.bt_state:
            # Write Command to Bluetooth COM Port
            self.bt_com.write(bytes(command + "\n",'utf-8'))

    ##### CONTROL PROTOCOLS #####

    # PROTOCOL : Capture
    def protocolCapture(self):
        # self.sendCommandBT("reset")
        self.sendCommandBT("capture")
        print("Clicking!")

    # PROTOCOL : Back
    def protocolBack(self):
        self.sendCommandBT("back")
        print("Back/Escape!")
    
    # PROTOCOL : Photo Mode
    def protocolPhotoMode(self):
        self.sendCommandBT("modePhoto")
        print("Switching to Photo Mode!")

    # PROTOCOL : Video Mode
    def protocolVideoMode(self):
        self.sendCommandBT("modeVideo")
        print("Switching to Video Mode!")

    # PROTOCOL : Nav Arrow Up
    def protocolNavUp(self):
        self.sendCommandBT("up")

    # PROTOCOL : Nav Arrow Down
    def protocolNavDown(self):
        self.sendCommandBT("down")

    # PROTOCOL : Nav Arrow Right
    def protocolNavRight(self):
        self.sendCommandBT("right")

    # PROTOCOL : Nav Arrow Left
    def protocolNavLeft(self):
        self.sendCommandBT("left")

    # PROTOCOL : Zoom In +
    def protocolZoomIn(self):
        self.sendCommandBT("+")
        print("Zooming In!")

    # PROTOCOL : Zoom Out -
    def protocolZoomOut(self):
        self.sendCommandBT("-")
        print("Zooming Out!")

    # PROTOCOL : Zoom x1
    def protocolZoomX1(self):
        self.sendCommandBT("zoomX1")
        print("Zoom x1!")

    # PROTOCOL : Zoom x10
    def protocolZoomX10(self):
        self.sendCommandBT("zoomX10")
        print("Zoom x10!")

    # PROTOCOL : Zoom x50
    def protocolZoomX50(self):
        self.sendCommandBT("zoomX50")
        print("Zoom x50!")

    # PROTOCOL : Zoom x100
    def protocolZoomX100(self):
        self.sendCommandBT("zoomX100")
        print("Zoom x100!")

    # PROTOCOL : Zoom -x1
    def protocolZoomMX1(self):
        self.sendCommandBT("zoomMX1")
        print("Zoom -x1!")

    # PROTOCOL : Zoom -x10
    def protocolZoomMX10(self):
        self.sendCommandBT("zoomMX10")
        print("Zoom -x10!")

    # PROTOCOL : Zoom -x50
    def protocolZoomMX50(self):
        self.sendCommandBT("zoomMX50")
        print("Zoom -x50!")

    # PROTOCOL : Zoom -x100
    def protocolZoomMX100(self):
        self.sendCommandBT("zoomMX100")
        print("Zoom -x100!")
    
    # Command Execution Unit
    def executeCommand(self, sender, data, command):
        # print(command)
        if command=="capture":
            self.protocolCapture()
        elif command=="back":
            self.protocolBack()

        elif command=="photo_mode":
            self.protocolPhotoMode()
        elif command=="video_mode":
            self.protocolVideoMode()

        elif command=="nav_up":
            self.protocolNavUp()
        elif command=="nav_down":
            self.protocolNavDown()
        elif command=="nav_right":
            self.protocolNavRight()
        elif command=="nav_left":
            self.protocolNavLeft()

        elif command=="zoom_in":
            self.protocolZoomIn()
        elif command=="zoom_out":
            self.protocolZoomOut()

        elif command=="zoom_x1":
            self.protocolZoomX1()
        elif command=="zoom_x10":
            self.protocolZoomX10() 
        elif command=="zoom_x50":
            self.protocolZoomX50()
        elif command=="zoom_x100":
            self.protocolZoomX100()

        elif command=="zoom_mx1":
            self.protocolZoomMX1()
        elif command=="zoom_mx10":
            self.protocolZoomMX10() 
        elif command=="zoom_mx50":
            self.protocolZoomMX50()
        elif command=="zoom_mx100":
            self.protocolZoomMX100()
            