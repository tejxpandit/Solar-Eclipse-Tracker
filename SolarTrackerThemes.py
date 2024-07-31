# File : Solar Tracker App Themes
# Author : Tej Pandit
# Date : July 2024

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
    