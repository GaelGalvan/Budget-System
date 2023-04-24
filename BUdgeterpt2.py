import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 
from customtkinter import *

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS userInfo(
    first_name text,
    last_name text,
    pronoun text,
    age integer
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS userPass(
    username text,
    password text
    
    
)""")



class MyFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        CTkButton(master = self.my_frame, text = "Login", command=self.login).grid(padx = 150,pady=20, row = 1, column=0)
        CTkButton(master = self.my_frame, text = "Register", command=self.register).grid(padx = 100,pady=10,row = 2, column=0)
        CTkButton(master = self.my_frame, text = "Show database", command=self.show).grid(pady=10)
    def show(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        data = cursor.execute("SELECT * FROM userInfo")
        table = ""
        for item in data:
            table += str(item) + "\n"
        CTkLabel(self.my_frame, text=table ).grid()
        data = cursor.execute("SELECT * FROM userPass")
        table = ""
        for item in data:
            table += str(item) + "\n"
        CTkLabel(self.my_frame, text=table ).grid()
        
    def login(self):
        login = Login()
        login.mainloop()
        
    def register(self):
        register = Register()
        register.mainloop()
class Login(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        CTkLabel(master = self.my_frame, text = "Username").grid(padx = 100, row = 1, column=0)
        self.username = CTkEntry(master=self.my_frame,placeholder_text="Username" )
        self.username.grid(row = 1, column=1)

        CTkLabel(master = self.my_frame, text = "Password").grid(padx = 100, row = 2, column=0)
        self.password = CTkEntry(master=self.my_frame,placeholder_text="Password" , show="*")
        self.password.grid(row = 2, column=1)
        CTkButton(master = self.my_frame, text="Login",command=self.verify).grid(row=3,padx=50,columnspan=2)
        
    def verify(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        # Execute the query and retrieve the result
        cursor.execute(f"SELECT username FROM userPass WHERE username='{self.username.get()}' AND password='{self.password.get()}'")
        result = cursor.fetchone()
        
        # Check if the result is None
        if result is not None:
            # If the result is not None, the username and password are correct
            print("Correct")
        else:
            tk.messagebox.showinfo('Error', 'Incorrect Username or Password')
        
        # Close the connection
        connection.close()
        
class Register(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.tab_view = MyRegisterTabs(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        
        

class MyRegisterTabs(CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

      
        self.add("Personal Information")
        self.add("Banking Information")
        self.add("Sign Up")

        # add widgets on tabs
        CTkLabel(master=self.tab("Personal Information") , text="First Name").grid(row=0, column=0, padx=20, pady=10)
        self.user_first_name = CTkEntry(master=self.tab("Personal Information"))
        self.user_first_name.grid(row=1,column=0)
        
        CTkLabel(master=self.tab("Personal Information") , text="Last Name").grid(row=0, column=1, padx=20, pady=10)
        self.user_last_name = CTkEntry(master = self.tab("Personal Information"),)
        self.user_last_name.grid(row = 1,column=1, padx=20)
        
        self.user_pronouns = CTkComboBox(master = self.tab("Personal Information"), values=["He/Him", "She/Her", "They/Them"])
        self.user_pronouns.grid(row = 0, column = 2)
        
        CTkLabel(master = self.tab("Personal Information"), text = "Age").grid(row = 2, column =0)
        self.user_age = CTkEntry(master = self.tab("Personal Information"))
        self.user_age.grid(row = 3 , column = 0)
        
        CTkLabel(master = self.tab("Banking Information"), text ="Checking account balance").grid(row=0,column=0)
        self.balance = CTkEntry(master = self.tab("Banking Information"))
        self.balance.grid(row=1,column=0)
        
        CTkLabel(master = self.tab("Banking Information"), text ="Savings account balance").grid(padx=50,row=0,column=1)
        self.savings = CTkEntry(master = self.tab("Banking Information"))
        self.savings.grid(row=1,column=1)
        
        CTkLabel(master = self.tab("Banking Information"), text ="Monthly income").grid(row=0,column=2)
        self.income = CTkEntry(master = self.tab("Banking Information"))
        self.income.grid(row=1,column=2)
        
        CTkLabel(master=self.tab("Banking Information"), text="Expenses").grid(row=2,column = 0)
        expense_name = CTkEntry(master = self.tab("Banking Information"))
        expense_name.grid(row= 3, column = 0)
        
        CTkLabel(master=self.tab("Banking Information"), text="Price of Expense").grid(row=2,column = 1)
        expense_name = CTkEntry(master = self.tab("Banking Information"))
        expense_name.grid(row= 3, column = 1)
        
        CTkButton(master=self.tab("Banking Information"), text="Add expense").grid(row=4,columnspan=2, pady=10)   
        
     
        
        
        
        CTkLabel(master = self.tab("Sign Up"), text = "Username").grid(row = 0 , column=0)
        self.user_username = CTkEntry(master= self.tab("Sign Up"))
        self.user_username.grid(row = 1, column=0)
        
        CTkLabel(master = self.tab("Sign Up"), text = "Password").grid(padx = 50, row = 0 , column=1) 
        self.user_password = CTkEntry(master= self.tab("Sign Up"))
        self.user_password.grid(row = 1, column=1)
        
        CTkButton(master=self.tab("Sign Up"), text="Submit",command=self.addDataToTable).grid(pady = 20,rowspan=2,columnspan=2)
        
        
    def addDataToTable(self):
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        try:
            cursor.execute("INSERT INTO userInfo VALUES (:first_name, :last_name,:pronoun,:age  )",
                        {
                            "first_name":self.user_first_name.get(),
                            "last_name":self.user_last_name.get(),
                            'pronoun':self.user_pronouns.get(),
                            'age':int(self.user_age.get())
                                
                        }) 
        except ValueError:
            tk.messagebox.showinfo('Error', 'Age field not properly filled')
            
        
        cursor.execute(f"SELECT username FROM userPass WHERE username='{self.user_username.get()}'")
        result = cursor.fetchone()
        
        # Check if the result is None
        if result is None and len(self.user_username.get()) >= 4:
            # If the result is not None, the username can be used
            cursor.execute("INSERT INTO userPass VALUES (:username, :password )",
                    {
                        "username":self.user_username.get(),
                        "password":self.user_password.get()
                            
                    }) 
        elif result is not None:
            tk.messagebox.showinfo('Error', 'Username Already Taken')
        else:
            tk.messagebox.showinfo('Error', 'Username Must Be More Then 4 Characters')
        
        
            
        connection.commit()
        connection.close()
        