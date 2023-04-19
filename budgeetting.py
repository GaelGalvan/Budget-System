import tkinter as tk
import os as os
class Budgeter():
    def __init__(self) -> None:
        
        self.root = tk.Tk()

        self.root.config(bg = "white")
        self.root.geometry("350x400")
        self.root.title("Budgeting app")
        tk.Label(text ="Budgeter", bg = "grey", width=200, height = 2).pack()
        self.screen1 = None
        self.screen2= None
        self.screen3 = None
        
        
        self.user_money = tk.IntVar()
        self.pass_verify = tk.StringVar()
        self.user_verify = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        self.balance = 0
        
        def login():
             
            self.screen2 = tk.Toplevel(self.root)
            self.screen2.geometry("350x300")
            self.screen2.title("Login")
            
            
            tk.Label(self.screen2, text ="Please enter info below").pack()
            tk.Label(self.screen2, text = "Login *").pack()
            tk.Entry(self.screen2,textvariable=self.user_verify).pack()
            tk.Label(self.screen2,text = "Password *").pack()
            tk.Entry(self.screen2, textvariable= self.pass_verify).pack()
            tk.Label(self.screen2, text ="").pack()
            tk.Button(self.screen2, text = "Login", height = 1, width = 10 ,command= login_check).pack()
        def register():
            self.screen1 = tk.Toplevel(self.root)
            self.screen1.geometry("250x250")
            
        
            
            tk.Label(self.screen1, text ="Please enter info below").pack()
            tk.Label(self.screen1, text = "Username *").pack()
            tk.Entry(self.screen1,textvariable= self.username).pack()
            tk.Label(self.screen1,text = "Password *").pack()
            tk.Entry(self.screen1, textvariable= self.password).pack()
            tk.Label(self.screen1, text ="").pack()
            tk.Button(self.screen1, text = "Register", height = 1, width = 10 ,command= user_register).pack()
            
            
        def user_register():
            file = open(self.username.get(), 'w')
            file.write(self.username.get() +"\n")
            file.write(self.password.get() +"\n")
            file.close()
        def login_check():
            user_log = self.user_verify.get()
            pass_log= self.pass_verify.get()
            
            list_of_files = os.listdir()
            if user_log in list_of_files:
                file1 = open(user_log, "r")
                verify = file1.read().splitlines()
                if pass_log in verify:
                    login_sucess()
                else:
                    wrong_pass()
            else:
                no_username()
        def no_username():
            tk.Label(self.screen2, text="Username not found").pack()
        def wrong_pass():
            tk.Label(self.screen2, text = "Incorrect password").pack()
        def login_sucess():
            session()
        def deposit():
            self.balance += self.user_money.get()
            tk.Label(self.screen3,text = f"User Balance = {self.balance}", height= 5).pack()
        def session():
            self.screen3 = tk.Toplevel(self.root)
            self.screen3.title = "Dashboard"
            self.screen3.geometry("800x800")
            self.screen3.config(bg='white')
            tk.Label(self.screen3 , text = "")
            
            tk.Entry(self.screen3, textvariable= self.user_money ).pack()
            
            tk.Button(self.screen3, text = "Deposit", command = deposit).pack()
            tk.Label(text = "", height= 20)
            tk.Button(self.screen3, text = "Calculate best savings plan according to 60/40 plan?" ,command = plan6040).pack(pady=50, side= tk.TOP, anchor="w")
        def plan6040():
            pass
            
            
        
            
            

            
            
        tk.Label(text = "" , background='white').pack()
        tk.Button(text = "login" , height=2, width=20, command = login).pack()
        tk.Label(text = "", bg ='white' ,).pack()
        tk.Button(text = "Register", height = 2, width = 20 , command= register).pack()

        self.root.mainloop()


bud = Budgeter()