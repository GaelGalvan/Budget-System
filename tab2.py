import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
from customtkinter import *
from PIL import Image   
height = 500

class HomeTab(CTk):
    def __init__(self):
        super().__init__()
        self.title("Budget Home")
        self.geometry("1200x680")
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.grid_rowconfigure((1,3), weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

        # Home Tab Before Entering

        # Left Frame
        self.welcomeLabel = CTkLabel(master = self, text="Welcome To The Budgeter", font = CTkFont(size = 30, weight = "bold")).grid(row = 0, column = 1, sticky = "nsew")
        self.tabLeftFrame = CTkFrame(master = self, width = 250).grid(row = 1, column = 0, padx = (0,20), sticky = "nsew")
        self.tabView = LeftTabbing(master = self.tabLeftFrame, width= 300).grid(row = 1, column = 0, padx = (0,20), sticky = "nsew")
        
        # Mid Frame with Image
        self.midFrame = CTkFrame(master = self, width = 100,height = 100, fg_color="transparent").grid(row = 1, column = 2, padx = (0,20), sticky = "nsew")
        self.HomeImage = CTkImage(Image.open(os.path.join(image_path, "Budgeter.png")), size=(350, 350))
        self.HomeLabel = CTkLabel(master = self.midFrame, text="", image=self.HomeImage)
        self.HomeLabel.grid(row = 1, column = 1, padx = (70,0))

        # Right Frame
        self.tabRightFrame = CTkFrame(master = self, width = 250).grid(row = 1, column = 5, padx = (20,0), sticky = "nsew")
        self.tabView2 = RightTabbing(master = self.tabLeftFrame, width= 300).grid(row = 1, column = 5, padx = (20,0), sticky = "nsew")

        #Start Button  
        self.startImage = CTkImage(dark_image=Image.open(os.path.join(image_path, "StartButton.png")), size=(150, 150))
        self.startFrame = CTkFrame(master = self, width = 0, height = 50)
        self.startFrame.grid_columnconfigure(2, weight = 1)
        self.startFrame.grid(row = 3, column = 0, columnspan = 10, sticky = "NSEW")
        self.startButton = CTkButton(master = self.startFrame,text="",image=self.startImage, command = self.start, width=100, fg_color="transparent")
        self.startButton.grid(row = 0, column = 2, padx = 20, pady = 20)

    def start(self):
        HomeTab.quit
        StartTab(isfs, theme, slider, appearance_window)
# Class which will hold tabs
class LeftTabbing(CTkTabview):
    def __init__(self, master, width, **kwargs):
        super().__init__(master, width, height, **kwargs)

        # All tabs
        self.add("Home")
        self.add("Settings")

        #Home Configuration 
        self.textbox = CTkTextbox(master = self.tab("Home"), width=250, height = 350)
        
        self.textbox.grid(row=0, column = 0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        with open('Text\\Home_Text.txt', 'r' ) as x:
            Text = x.read()
            self.textbox.insert("0.0",Text)
        self.textbox.configure(state = "disabled")

        # Settings Configuration
        CTkLabel(master = self.tab("Settings"), text = "Set Apperance Option", font = CTkFont(size = 15)).grid(row = 0, column = 0, padx = (50,0), pady = (20,0))
        self.appearance_option = CTkOptionMenu(master = self.tab("Settings"), values=["Pick","System Default", "Dark", "Light"], command=self.changeAppearance)
        self.appearance_option.grid(row = 1, column = 0, padx = (60,0), pady = (0,20))

        CTkLabel(master = self.tab("Settings"), text = "Fullscreen Upon Starting", font = CTkFont(size = 15)).grid(row = 3, column = 0, padx = (50,0), pady =(20,0))
        self.color_theme = CTkOptionMenu(master = self.tab("Settings"), values = ["Pick","Yes","No"], command=self.isFullscreen)
        self.color_theme.grid(row = 4, column = 0, padx = (60,0), pady = (0,20))

        CTkLabel(master = self.tab("Settings"), text = "Color Theme", font = CTkFont(size = 15)).grid(row = 5, column = 0, padx = (50,0), pady = (20,0))
        self.color_theme = CTkOptionMenu(master = self.tab("Settings"), values = ["Pick","Blue","Green", "Dark Blue"], command=self.setTheme)
        self.color_theme.grid(row = 6, column = 0, padx = (60,0), pady = (0,20))

        CTkLabel(master = self.tab("Settings"), text = "Scaling", font = CTkFont(size = 15)).grid(row = 8, column = 0, padx = (50,0), pady = (20,0))
        self.slider_1 = CTkSlider(master = self.tab("Settings"), from_=0, to=3, number_of_steps=4, command=self.sliderVal)
        self.slider_1.grid(row = 9, column = 0, padx = (60,0), pady = (0,20))



    def changeAppearance (self, mode : str):
        global appearance_window
        if mode == "Pick":
            pass
        if mode == "System Default":
            appearance_window = "System"
        else:
            appearance_window = mode
     
    def isFullscreen(self, mode : str):
        global isfs
        if mode == "Yes":
            isfs = True
        else:
            isfs = False
    def sliderVal(self, mode : int):
        global slider
        slider = mode
    def setTheme(self, mode : str):
        global theme 
        if mode == "Blue":
            theme = "blue"
        elif mode == "Green":
            theme =  "green"
        elif mode == "Dark Blue":
            theme = "dark-blue"


class RightTabbing(CTkTabview):
    def __init__(self, master, width, **kwargs):
        super().__init__(master, width, height, **kwargs)

        #All tabs
        self.add("Purpose")
        self.add("More Info")

        
        # Purpose Configuration
        self.textbox = CTkTextbox(master = self.tab("Purpose"), width=250, height = 350)
        
        self.textbox.grid(row=0, column = 0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        with open('Text\\Purpose_Text.txt', 'r' ) as x:
            Text = x.read()
            self.textbox.insert("0.0",Text)
        self.textbox.configure(state = "disabled")
        # More Info Configuration
        CTkLabel(master = self.tab("More Info"), text = "Contact Us", font = CTkFont(size = 15)).grid(row = 0, column = 1, padx = (0,75), pady = (20,0))

        CTkLabel(master = self.tab("More Info"), text = "Gael Galvan:", font = CTkFont(size = 15)).grid(row = 1, column = 0, padx = (40,0), pady = (20,0))
        CTkLabel(master = self.tab("More Info"), text="gaelgalvan12@gmail.com",font= CTkFont(size=15, underline=True)).grid(row = 1, column = 1, padx = (10,0), pady = (20,0))

        CTkLabel(master = self.tab("More Info"), text = "Angel Escobedo:", font = CTkFont(size = 15)).grid(row = 2, column = 0, padx = (40,0), pady = (20,0))
        CTkLabel(master = self.tab("More Info"), text="angel.escobedo03@utrgv.edu",font= CTkFont(size=15, underline=True)).grid(row = 2, column = 1, padx = (10,0), pady = (20,0))

        CTkLabel(master = self.tab("More Info"), text = "Diego Esparza:", font = CTkFont(size = 15)).grid(row = 3, column = 0, padx = (40,0), pady = (20,0))
        CTkLabel(master = self.tab("More Info"), text="testemail123@gmail.com",font= CTkFont(size=15, underline=True)).grid(row = 3, column = 1, padx = (10,0), pady = (20,0))

        CTkLabel(master = self.tab("More Info"), text = "David Garza:", font = CTkFont(size = 15)).grid(row = 4, column = 0, padx = (40,0), pady = (20,0))
        CTkLabel(master = self.tab("More Info"), text="dgarz321@gmail.com",font= CTkFont(size=15, underline=True)).grid(row = 4, column = 1, padx = (10,0), pady = (20,0))
class StartTab(CTk):
    def __init__(self, isFullScreen, CTheme, slider, appearance):
        super().__init__()
        print(f"Fullscreen: {isFullScreen}, Theme: {CTheme}, Slider: {slider}, Appearance: {appearance}")
        self.title("Budgeter")
        self.geometry("1100x580")
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.grid_rowconfigure((1), weight=1)

if __name__ == "__main__":
    app = HomeTab()
    app.resizable(False,False)
    app.mainloop()