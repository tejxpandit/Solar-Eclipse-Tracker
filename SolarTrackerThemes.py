# File : Solar Tracker App Themes
# Author : Tej Pandit
# Date : August 2024

import dearpygui.dearpygui as dpg

class SolarTrackerThemes:
    def __init__(self):
        self.varName = None

    def navBlue(self):
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Button, 			(48, 100, 153, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,   (84, 159, 235, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,    (84, 159, 235, 200))
        return theme
    
    def captureGreen(self):
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Button, 			(19, 79, 43, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,   (10, 46, 25, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,    (10, 46, 25, 200))
        return theme

    def enableGreen(self):
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Button, 			(82, 167, 27, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,   (48, 99, 15, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,    (48, 99, 15, 200))
        return theme

    def disableRed(self):
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Button, 			(167, 55, 27, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,   (84, 27, 13, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,    (84, 27, 13, 200))
        return theme