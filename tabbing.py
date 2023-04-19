import tkinter as tk
from tkinter import ttk
import os as os
from budgeter_2 import *
from customtkinter import *

#initial page
# main window
root = Tk()
root.geometry(f"800x600")

# tab control and padding

style = ttk.Style()
root.title("Budget System")
style.configure('TNotebook.Tab', font=('Helvetica', '18', 'bold'))
tab_control = ttk.Notebook(root, style='TNotebook')

# Home tab
home_tab = ttk.Frame(tab_control)
tab_control.add(home_tab, text='              Home               ')

# About tab
about_tab = ttk.Frame(tab_control)
tab_control.add(about_tab, text='             About               ')

# Contact tab
contact_tab = ttk.Frame(tab_control)
tab_control.add(contact_tab, text='              Contact              ')

# widgets
home_title = tk.Label(home_tab, text="Welcome to our website!", font=("Helvetica", 24), padx=20, pady=20)
home_title.pack()
home_content = Window1(home_tab)
home_content.btnReg.pack()
home_content.b2.pack()
home_content.b3.pack()

# widgets
about_title = tk.Label(about_tab, text="About Us", font=("Helvetica", 24), padx=20, pady=20)
about_title.pack()
about_content = tk.Label(about_tab, text="We are cool", font=("Helvetica", 18), padx=20, pady=20)
about_content.pack()

# widgets
contact_title = tk.Label(contact_tab, text="Contact Us", font=("Helvetica", 24), padx=20, pady=20)
contact_title.pack()
contact_content = tk.Label(contact_tab, text="contact us at @ourwebsite.com", font=("Helvetica", 18), padx=20, pady=20)
contact_content.pack()

# tab control
tab_control.pack(expand=1, fill="both")

# main loop
root.mainloop()