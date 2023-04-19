from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3 
height = 500
width = 500

'''
How I created the sqlite table uncomment this if your gonna run it for the first time and then recooment it out so the table isnt brand new everytime

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE userInfo(
    first_name text,
    last_name text,
    pronoun text,
    age integer,
    monthly_income real
    
)""")

cursor.execute("""CREATE TABLE userPass(
    username text,
    password text
    
    
)""")

'''

    
def main():
    
    
    root = Tk()
    app = Window1(root)
    root.mainloop()
#initial page
class Window1:
    def __init__(self, master):

        self.btnReg = Button(master, height = 3 , width=15,bg="white", text="Register", command=self.register)
        self.b2 = Button(master, height=3, width=15,bg="white", text="Login",command=self.login )
        self.b3 = Button(master, height=3, width=7,bg="white", text="show db",command=self.show )
        
        
    def register(self):
        newWindow = Tk()
        app = Register(newWindow)
    def login(self):
        newWindow = Tk()
        app = Login(newWindow)
    def show(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        data = cursor.execute("SELECT * FROM userInfo")
        table = ""
        for item in data:
            table += str(item) + "\n"
        Label(self.frame, text=table ).grid(columnspan=2, rowspan=2)
        
        table = ""
        data = cursor.execute("SELECT * FROM userPass")
        for item in data:
            table += str(item) + "\n"
        Label(self.frame, text=table ).grid(columnspan=2, rowspan=2)
        
       
        
        connection.commit()
        connection.close()


        
        

        
class HomePage:
    def __init__(self,master):
        self.master = master
        self.master.config(bg = "white")
        self.master.title("HomePage")
        self.master.geometry(f"{height}x{width}")
        Label(self.master,text ="",height=1,bg="white" ).pack()
        
        self.notebook = ttk.Notebook(self.master)
       
        self.welcome_tab = Frame(self.notebook, bg = "white")
        Label(self.welcome_tab,bg = "white", text="Hello and welcome").pack()
       
        
        self.graphs_tab = Frame(self.notebook, bg = "white")
        Label(self.graphs_tab, text="This is gonna be a graph of your spending ").pack()
        
        
        self.welcome_tab.pack(fill= "both", expand=1)
        
        self.notebook.add(self.welcome_tab, text= "Welcome")
        self.notebook.add(self.graphs_tab, text="Graphs")
        self.notebook.pack()
        
    
        
        
class Register:
    def __init__(self, master):
        self.user_subscription_and_price = {}
        self.user_expense_and_price = {}
        self.providers = []
        
        self.master = master
        self.master.config(bg = "white")
        self.master.title("Registration Page")
        self.master.geometry(f"{height}x{width}")
        #creating master frame that other frames live inside
        self.notebook = ttk.Notebook(self.master)
        self.user_lFrame = Frame(self.notebook)
        self.user_lFrame.pack(fill= "both", expand=1)
        
        self.user_info_frame = LabelFrame(self.user_lFrame)
        self.user_info_frame.pack()
        
        
        
        first_name_label = Label(self.user_info_frame, text = "First Name")
        last_name_label = Label(self.user_info_frame,text = "Last Name")
        pronouns_label = Label(self.user_info_frame, text = "Pronouns")
        self.pronouns = ttk.Combobox(self.user_info_frame, values =["He", "Her", "They"])
        self.first_name_entry = Entry(self.user_info_frame)
        self.last_name_entry = Entry (self.user_info_frame)
        Label(self.user_info_frame, text = "Age").grid(row = 2,column=0)
        self.age = Spinbox(self.user_info_frame, from_= 18 , to=100)
        
        first_name_label.grid(row = 0, column=0)
        last_name_label.grid(row =0, column=1)
        pronouns_label.grid(row = 0, column=2)
        self.first_name_entry.grid(row = 1, column=0)
        self.last_name_entry.grid(row = 1, column=1)
        self.pronouns.grid(row= 1, column=2)
        self.age.grid(row = 3, column=0)
        
        for wid in self.user_info_frame.winfo_children():
            wid.grid_configure(padx=1,pady=5)
        self.user_fFRame = Frame(self.notebook)
        self.user_finance_info = LabelFrame(self.user_fFRame)
        self.user_finance_info.pack()
        #Label frame to display users subscriptions as they sign up
        self.display_sub = LabelFrame(self.user_finance_info )
        #widgets for 2nd tab
        Label(self.user_finance_info,text = "Enter your Subscription").grid(row = 0, column=0)
        self.current_subscription = Entry(self.user_finance_info)
        Label(self.user_finance_info, text = "Price of Subscription per month").grid(row = 0 , column=1)
        self.sub_price = Entry(self.user_finance_info,)
        Button( self.user_finance_info, text = "Add Subscription", command= self.add_subscription).grid(row=2,column=0)
        Label(self.user_finance_info, text = "Current Subscriptions").grid(row =0, column=2) 
        
        Label(self.user_finance_info, text = "Enter Monthly Expense").grid(row= 3, column=0)
        self.current_expense = Entry(self.user_finance_info)
        self.current_expense.grid(row= 4, column=0)
        Label(self.user_finance_info, text = "Enter Price of Monthly Expense").grid(row= 3, column=1)
        self.current_expense_price = Entry(self.user_finance_info)
        self.current_expense_price.grid(row=4,column=1 )
        
        
        Label(self.user_finance_info, text="Monthly Income" ).grid(row =5 , column=0 )
        self.monthly_income = Entry(self.user_finance_info)
        Label(self.user_finance_info, text = "Current Bank Balance: ").grid(row = 5, column=1)
        self.bank_balance = Entry(self.user_finance_info)
        
        
        
        
        
        self.bank_balance.grid(row = 6, column=1)
        self.current_subscription.grid(row=1, column=0)
        self.sub_price.grid(row = 1, column=1)
        self.display_sub.grid(row = 1, column = 2 , sticky = "news")
        self.monthly_income.grid(row=6,column=0)
        
        
        for wid in self.user_finance_info.winfo_children():
            wid.grid_configure(padx=3,pady=5)
            
            
        #3rd tab for users to confirm and register
        self.user_cFrame = Frame(self.notebook)
        self.confirm_frame = LabelFrame(self.user_cFrame)
        self.confirm_frame.pack()
        Label(self.confirm_frame, text ="Username: ", ).grid(row= 0 , column= 0)
        Label(self.confirm_frame, text="Password* ").grid(row=0,column=1)
        self.username = Entry(self.confirm_frame)
        self.password = Entry(self.confirm_frame)
        self.username.grid(row=1, column=0)
        self.password.grid(row = 1, column=1)
        
        Button(self.confirm_frame, text="Register", command=self.confirm).grid(row= 2 ,columnspan=2)

       
        
        
        
        self.notebook.add(self.user_lFrame, text="User Info")
        self.notebook.add(self.user_fFRame, text = "Info frame")
        self.notebook.add(self.user_cFrame, text="Confirm")
        self.notebook.pack()
        
        
        #for when users register 
    def add_subscription(self):
        self.user_subscription_and_price[self.current_subscription.get()] = self.sub_price.get()
        self.providers.append(self.current_subscription.get())
        for i in range(len(self.providers)):
            Label(self.display_sub,text = f"{self.providers[i]}").grid(row = i, column=0)
        #clear text boxes
        self.sub_price.delete(0,END)
        self.current_subscription.delete(0,END)
    
    
    def confirm(self):
        new_window = Toplevel(self.master )
        self.confirm_window = Confirm(new_window, 
    self.first_name_entry.get(), self.last_name_entry.get(), self.pronouns.get(), self.age.get(), self.monthly_income.get(), self.providers,self.username.get(), self.password.get() )
        
        
class Confirm:
    def __init__(self, master, first_name, lastName, pronoun,age,monthly_income,subscription,username, password ):
        
        self.master = master
        self.master.config(bg = "white")
        self.master.title("Confirm")
        self.master.geometry("250x200")
        
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0)
        self.frame.pack()
        self.user_fields_frame = LabelFrame(self.frame)
        
        self.user_fields_frame.grid(row=1,column=0)
        
        self.title = Label(self.frame, text ="Conformation Page", width = 30)
        Label(self.user_fields_frame, text = f"Name: {first_name} {lastName}").grid(row=0,column=0)
        Label(self.user_fields_frame, text = f"Pronouns: {pronoun}").grid(row=1,column=0)
        Label(self.user_fields_frame, text = f"Age: {age}").grid(row=2,column=0)
        Label(self.user_fields_frame, text = f"Monthly Income: {monthly_income}").grid(row=3,column=0)
        Label(self.user_fields_frame, text= f"Subscriptions").grid(row=0,column=1)
        for i,v in enumerate(subscription,1):
            Label(self.user_fields_frame, text = v, ).grid(row  = i, column=1)
        
        
        Button(self.frame, text="Confirm", command=lambda:[self.homepage(), 
                self.addDataToTable(first_name, lastName, pronoun, int(age),float(monthly_income), username, password)]).grid(row=4,column=0)
        Button(self.frame, text= "Decline", command=self.reset).grid(row=5, column=0)
        
        
        self.title.grid(row = 0, column=0)
        
    def homepage(self):
        new_window = Toplevel(self.master)
        self.HOME = HomePage(new_window)
        
        
        
        
        
    def addDataToTable(self, first_name, lastName, pronoun, monthly_income, age, username, password):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO userInfo VALUES (:first_name, :last_name,:pronoun,:age , :monthly_income )",
                       {
                           "first_name":first_name,
                           "last_name":lastName,
                           'pronoun':pronoun,
                           'age':age,
                           'monthly_income': monthly_income
                           
                       }) 
        cursor.execute("INSERT INTO userPass VALUES(:username, :password)",
                       {
                           "username": username,
                           'password':password
                       })
        connection.commit()
        connection.close()
        
    def reset(self):

        app = Toplevel(self.master)
        setted = Register(app)
        

class Login():
    def __init__(self, master) :
        self.master = master
        self.master.config(bg = "white")
        self.master.title("Login Page")
        self.master.geometry(f"{height}x{width}")
        
        self.frame = Frame(self.master)
        self.frame.config(bg= "white")
        self.frame.pack()
        
        drop_menu = StringVar()
        drop_menu.set("Nothing")
        
        
        OptionMenu(self.frame, drop_menu,"Register" ).grid(row=0, column=0)
        
        Label(self.frame, text ="",bg= "white", height = 3, width = 20 ).grid(column=0,row=1)
        Label(self.frame, text ="Username:"  ,bg="white").grid(column=0,row=1)
        self.current_user = Entry(self.frame )
        self.current_user.grid(row=1,column=1)
        Label(self.frame, text ="Password:"  ,bg="white").grid(column=0,row=2)
        self.current_pass = Entry(self.frame, )
        self.current_pass.grid(row=2,column=1)
        Button(self.frame, text= "Login", command=self.verify).grid(column = 1, row = 4)
        
        
    def homepage(self):
        new_window = Toplevel(self.master)
        self.HOME = HomePage(new_window)

    def verify(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        # Execute the query and retrieve the result
        cursor.execute(f"SELECT username FROM userPass WHERE username='{self.current_user.get()}' AND password='{self.current_pass.get()}'")
        result = cursor.fetchone()
        
        # Check if the result is None
        if result is not None:
            # If the result is not None, the username and password are correct
            self.homepage()
        else:
            # If the result is None, the username and/or password is incorrect
            messagebox.showinfo('Error', 'Incorrect Username or Password')
        
        # Close the connection
        connection.close()

        
        
      
            
        
        
        
'''
calculator,

'''
        
        
        
            
        
        
        
        
        
   
        
        
       
        
        
        
    
    
if __name__ == '__main__':
    main()
    
   