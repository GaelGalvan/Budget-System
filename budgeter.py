from tkinter import *
from tkinter import ttk

class Window1:
    def register(self):
        self.newWindow = Tk()
        self.app = Register(self.newWindow)
    def __init__(self, master):
        self.btnReg = Button(master, height = 3 , width=15,bg="grey", text="Register", command=self.register)
        

        

class Confirm:
    def __init__(self, master, name, lastName, pronoun,age,income,subscription):
        self.master = master
        self.master.config(bg = "white")
        self.master.title("Confirm")
        self.master.geometry("250x200+0+0")
        
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0)
        self.frame.pack()
        self.user_fields_frame = LabelFrame(self.frame)
        
        self.user_fields_frame.grid(row=1,column=0)
        
        self.title = Label(self.frame, text ="Confirmation Page", width = 30)
        Label(self.user_fields_frame, text = f"Name: {name} {lastName}").grid(row=0,column=0)
        Label(self.user_fields_frame, text = f"Pronouns: {pronoun}").grid(row=1,column=0)
        Label(self.user_fields_frame, text = f"Age: {age}").grid(row=2,column=0)
        Label(self.user_fields_frame, text = f"Monthly Income: {income}").grid(row=3,column=0)
        Label(self.user_fields_frame, text= f"Subscriptions: {subscription}").grid(row=4,column=0)
        
        Label(self.frame, text = "If this look correct to please press confirm").grid(row=3,column=0)
        Button(self.frame, text="CONFIRM").grid(row=4,column=0)
        
        
        self.title.grid(row = 0, column=0)
        
        

        
class Register:
    def __init__(self, master):
        self.user_subscription_and_price = {}
        self.providers = []
        
        self.master = master
        self.master.config(bg = "black")
        self.master.title("Session")
        self.master.geometry("800x600+0+0")
        #creating master frame that other frames live inside
        self.frame = Frame(self.master)
        self.frame.pack()
    
        self.user_info_frame = LabelFrame(self.frame)
        self.user_info_frame.grid(row = 0 , column= 0, padx=20,pady=10 )
       
        
        #widgets for first frame
        first_name_label = Label(self.user_info_frame, text = "First Name")
        last_name_label = Label(self.user_info_frame,text = "Last Name")
        pronouns_label = Label(self.user_info_frame, text = "Pronouns")
        self.pronouns = ttk.Combobox(self.user_info_frame, values =["He/Him", "She/Her", "They/Them"])
        self.first_name_entry = Entry(self.user_info_frame)
        self.last_name_entry = Entry (self.user_info_frame)
        age_label = Label(self.user_info_frame, text = "Age")
        self.age = Spinbox(self.user_info_frame, from_= 18 , to=100)
        
        
        first_name_label.grid(row = 0, column=0)
        last_name_label.grid(row =0, column=1)
        pronouns_label.grid(row = 0, column=2)
        self.first_name_entry.grid(row = 1, column=0)
        self.last_name_entry.grid(row = 1, column=1)
        self.pronouns.grid(row= 1, column=2)
        age_label.grid(row = 2, column=0,)
        self.age.grid(row = 3, column=0)
        #adding a padding to all widgets to look cleaner
        for wid in self.user_info_frame.winfo_children():
            wid.grid_configure(padx=1,pady=5)
            
        #creating 2nd frame
        self.user_finance_info = LabelFrame(self.frame)
        self.user_finance_info.grid(row=1, column=0 , sticky="news", padx=20,pady=20)
        #Label frame to display users subscriptions as they sign up
        self.display_sub = LabelFrame(self.user_finance_info )
        #widgets for 2nd frame
        subscription_label = Label(self.user_finance_info,text = "Enter your Subscription")
        self.current_subscription = Entry(self.user_finance_info)
        price = Label(self.user_finance_info, text = "Price of Subscription per month")
        self.sub_price = Entry(self.user_finance_info,)
        self.add_sub = Button( self.user_finance_info, text = "Add Subscription", command= self.add_subscription)
        Subscription = Label(self.user_finance_info, text = "Current Subscriptions")
        monthly_income_label = Label(self.user_finance_info, text="Enter your monthly income" )
        self.monthly_income = Entry(self.user_finance_info)
        
        subscription_label.grid(row = 0, column=0)
        self.current_subscription.grid(row=1, column=0)
        self.add_sub.grid(row=2,column=0)
        self.sub_price.grid(row = 1, column=1)
        price.grid(row = 0 , column=1)
        Subscription.grid(row =0, column=2)
        self.display_sub.grid(row = 1, column = 2 , sticky = "news")
        monthly_income_label.grid(row =3 , column=0 )
        self.monthly_income.grid(row=4,column=0)
        
        for wid in self.user_finance_info.winfo_children():
            wid.grid_configure(padx=3,pady=5)
            
        #3rd frame for users to confirm and register
        self.confirm_frame = LabelFrame(self.frame)
        self.confirm_frame.grid(row=2,column=0)
        
        confirm_btn = Button(self.confirm_frame, text="Register", command=self.confirm)
        confirm_btn.grid(row= 0 ,column=0)
        
        #for when users register 
    def add_subscription(self):
        self.user_subscription_and_price[self.current_subscription.get()] = self.sub_price.get()
        self.providers.append(self.current_subscription.get())
        for i in range(len(self.providers)):
            b = Label(self.display_sub,text = f"{self.providers[i]}")
            b.grid(row = i, column=0)
    
    def confirm(self):
        self.new_window = Toplevel(self.master )
        self.confirm_window = Confirm(self.new_window, self.first_name_entry.get(), self.last_name_entry.get(), self.pronouns.get(), self.age.get(), self.monthly_income.get(), self.user_subscription_and_price)
        
    
