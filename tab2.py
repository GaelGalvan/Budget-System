import tkinter as tk
from tkinter import ttk
import os as os
from budgeter_2 import *
from customtkinter import *


class StartTab(CTk):
    def __init__(self):
        super().__init__()
        self.title("Budget Home")
        self.geometry("1100x580")
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.grid_rowconfigure((1), weight=1)

        # Home Tab Before Entering
        self.welcomeLabel = CTkLabel(master = self, text="Welcome To The Home Screen", font = CTkFont(size = 30, weight = "bold")).grid(row = 0, column = 1, sticky = "nsew")
        self.tabLeftFrame = CTkFrame(master = self, width = 250).grid(row = 1, column = 0, padx = (20,0), sticky = "nsew")
        self.tabView = LeftTabbing(master = self.tabLeftFrame, width= 300).grid(row = 1, column = 0, padx = (10,0), sticky = "nsew")
        self.tabRightFrame = CTkFrame(master = self, width = 250).grid(row = 1, column = 5, padx = (20,0), sticky = "nsew")
        self.tabView = RightTabbing(master = self.tabLeftFrame, width= 300).grid(row = 1, column = 5, padx = (10,0), sticky = "nsew")
        
# Class which will hold tabs
class LeftTabbing(CTkTabview):
    def __init__(self, master, width, **kwargs):
        super().__init__(master, width, height, **kwargs)

        # All tabs
        self.add("Home")
        self.add("Settings")

        # Each tab configuration
        CTkLabel(master = self.tab("Settings"), text = "Set Apperance Option", font = CTkFont(size = 15)).grid(row = 0, column = 0, padx = (50,0))
        self.appearance_option = CTkOptionMenu(master = self.tab("Settings"), values=["System Default", "Dark", "Light"], command=self.changeAppearance)
        self.appearance_option.grid(row = 1, column = 0, padx = (60,0))

        CTkLabel(master = self.tab("Settings"), text = "Fullscreen Upon Starting", font = CTkFont(size = 15)).grid(row = 3, column = 0, padx = (50,0))
        self.color_theme = CTkOptionMenu(master = self.tab("Settings"), values = ["Yes","No"], command=self.isFullscreen)
        self.color_theme.grid(row = 4, column = 0, padx = (60,0) )

        CTkLabel(master = self.tab("Settings"), text = "Color Theme", font = CTkFont(size = 15)).grid(row = 3, column = 0, padx = (50,0))
        self.color_theme = CTkOptionMenu(master = self.tab("Settings"), values = ["Blue","Green", "Dark Blue"], command=self.isFullscreen)
        self.color_theme.grid(row = 4, column = 0, padx = (60,0) )

        CTkLabel(master = self.tab("Settings"), text = "Scaling", font = CTkFont(size = 15)).grid(row = 8, column = 0, padx = (50,0))
        self.slider_1 = CTkSlider(master = self.tab("Settings"), from_=0, to=4, number_of_steps=4)
        self.slider_1.grid(row = 9, column = 0, padx = (60,0))



    def changeAppearance (self, mode : str):
        if mode == "System Default":
            set_appearance_mode("System")
        else:
            set_appearance_mode(mode)
    def isFullscreen(self, mode : str):
        if mode == "Yes":
            self.isfs = True
        else:
            self.isfs = False
    def sliderval(self, mode : int):
        self.slider = mode
    def setTheme(self, mode : str):
        if mode == "Blue":
            self.theme = "blue"
        elif mode == "Green":
            self.theme =  "green"
        elif mode == "Dark Blue":
            self.theme = "dark-blue"



class RightTabbing(CTkTabview):
    def __init__(self, master, width, **kwargs):
        super().__init__(master, width, height, **kwargs)

        #All tabs
        self.add("Purpose")
        self.add("More Info")

        # Each tab configuration
        
if __name__ == "__main__":
    app = StartTab()
    app.mainloop()