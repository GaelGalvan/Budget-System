import tkinter as tk
from tkinter import ttk
import os as os
from budgeter_2 import *
from customtkinter import *

set_default_color_theme("green")



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
        CTkLabel(master = self.tab("Home")).grid(row = 0, column = 0, padx = (50,0))
        self.appearance_option = CTkOptionMenu(master = self.tab("Settings"), values=["Default", "Dark", "Light"], command=self.changeAppearance)
        self.appearance_option.grid(row = 0, column = 1, padx = (50,0))
    def changeAppearance (self, mode : str):
        if mode == "Default":
            set_appearance_mode("System")
        else:
            set_appearance_mode(mode)

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