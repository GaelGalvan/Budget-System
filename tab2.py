from imports import *

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS userInfo(
    username text,
    password text,
    first_name text,
    last_name text,
    pronoun text,
    age integer,
    accountBalance real,
    savingBalance real,
    monthlyIncome real
    
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS user_goals (
    username text,
    goal text 
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
    username text,
    expense text,
    expense_price real,
    subscription text,
    subscription_price real
)""")
connection.commit()
connection.close()


class HomeTab(CTk):
    def __init__(self,username):
        height = 500
        self.user = username
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
        self.startImage = CTkImage(Image.open(os.path.join(image_path, "StartButton.png")), size=(150, 150))
        self.startFrame = CTkFrame(master = self, width = 0, height = 50)
        self.startFrame.grid_columnconfigure(2, weight = 1)
        self.startFrame.grid(row = 3, column = 0, columnspan = 10, sticky = "NSEW")
        self.startButton = CTkButton(master = self.startFrame,text="",image=self.startImage, command = self.start, width=100, fg_color="transparent")
        self.startButton.grid(row = 0, column = 2, padx = 20, pady = 20)

    def start(self):
        user = self.user
        self.destroy()
        # isfs, theme, slider, appearance_window setup 
        page = MainPage(user = user, isfs=isfs, theme=theme, slider=slider, appearance_window=appearance_window)
        page.mainloop()

# Class which will hold tabs
class LeftTabbing(CTkTabview):
    def __init__(self, master, width, **kwargs):
        super().__init__(master, width, height = 500, **kwargs)

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

        CTkLabel(master = self.tab("Settings"), text = "Fullscreen / Resizable Upon Starting", font = CTkFont(size = 15)).grid(row = 3, column = 0, padx = (50,0), pady =(20,0))
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
        if mode == 0:
            slider = 0.8
        elif mode == 0.75:
            slider = 0.9
        elif mode == 1.5:
            slider = 1.0
        elif mode == 2.25:
            slider = 1.1
        elif mode == 3.0:
            slider = 1.2


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
        super().__init__(master, width, height = 500, **kwargs)

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

class MyFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class MainPage(CTk):
    def __init__(self, user,isfs, theme, slider, appearance_window):
        super().__init__()
        # Sets up what was previously set in settings
        set_appearance_mode(appearance_window)
        set_default_color_theme(theme)
        set_widget_scaling(slider)
        if (isfs):
            self.winWidth = str(int(self.winfo_screenwidth()))
            self.winHeight = str(int(self.winfo_screenheight()))
            self.geometry(f"{self.winWidth}x{self.winHeight}")
            self.span = int(self.winWidth)
        else:
            self.span = 1200
            self.geometry("1200x680")
            self.resizable(False,False)

        #SQL connection
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        # Formatting
        self.user = user
        self.columnconfigure(0, weight = 1)
        self.topFrame = CTkFrame(master = self, height = 50, width = (self.span))
        self.topFrame.grid(row = 0, column = 0, columnspan = 3, sticky = "nsew")
        self.homeButton = CTkButton(self.topFrame, corner_radius=0, height=40,width = (self.span / 3), border_spacing=10, text="Home", fg_color="transparent")
        self.homeButton.grid(row = 0, column = 0)

        self.ExpensesButton = CTkButton(self.topFrame, corner_radius=0, height=40, width = (self.span / 3),border_spacing=10, text="Expenses", fg_color="transparent")
        self.ExpensesButton.grid(row = 0, column = 1)

        self.graphButton = CTkButton(self.topFrame, corner_radius=0, height=40, width = (self.span / 3), border_spacing=10, text="Graph", fg_color="transparent")
        self.graphButton.grid(row = 0 , column = 2)

        self.balance = cursor.execute(f"SELECT accountBalance FROM userInfo WHERE username = '{self.user}';")
        self.balance = cursor.fetchone()[0]



        self.balanceLabel = CTkLabel(self.topFrame, corner_radius = 0, text=f"${int(self.balance):,d}",text_color = "white",  font=CTkFont(family = "bookman", size=50, weight="bold"))
        self.balanceLabel.grid(row = 2, column = 1) 

        self.balance = cursor.execute(f"SELECT SavingBalance FROM userInfo WHERE username = '{self.user}';")
        self.balance = cursor.fetchone()[0]

        self.savingsFrame = CTkFrame(master = self, height = 50, width = (self.span),fg_color="white", bg_color=theme)
        self.savingsFrame.grid(row = 4, column = 0, columnspan = 3, sticky = "nsew")
        self.savingsLabel1 = CTkLabel(self.savingsFrame, corner_radius=0, text = "Savings:", text_color="black",font=CTkFont(family = "bookman", size=35, weight="bold"))
        self.savingsLabel1.grid(row = 0, column = 0, padx = 20)
        self.savingsLabel2 = CTkLabel(self.savingsFrame, corner_radius=0, text=f"${int(self.balance):,d}", text_color="black",font=CTkFont(family = "bookman", size=35, weight="bold"))
        self.savingsLabel2.grid(row = 0, column = 2, padx = (100, 0), sticky = "e")

        self.balance = cursor.execute(f"SELECT monthlyIncome FROM userInfo WHERE username = '{self.user}';")
        self.balance = cursor.fetchone()[0]

        self.incomeLabel1 = CTkLabel(self.savingsFrame, corner_radius=0, text = "Income:", text_color="black",font=CTkFont(family = "bookman", size=35, weight="bold"))
        self.incomeLabel1.grid(row = 1, column = 0, padx = 20)
        self.incomeLabel2 = CTkLabel(self.savingsFrame, corner_radius=0, text=f"${int(self.balance):,d}", text_color="black",font=CTkFont(family = "bookman", size=35, weight="bold"))
        self.incomeLabel2.grid(row = 1, column = 2, padx = (100, 0), sticky = "e")
        
        self.beginExpenseFrame = CTkFrame(master = self, height = 50, width = (self.span))
        self.beginExpenseFrame.grid(row = 5, column = 0)
        self.ExpenseLabel = CTkLabel(self.beginExpenseFrame, corner_radius = 0, text="Expenses",  font=CTkFont(family = "bookman", size=20, weight="bold"))
        self.ExpenseLabel.grid(row = 2, column = 1) 
        
        self.balance = cursor.execute(f"SELECT expense_price FROM expenses WHERE username = '{self.user}';")
        self.expenseName = cursor.execute(f"SELECT expense FROM expenses WHERE username = '{self.user}';")

        self.expenseFrame = CTkFrame(master = self, height = 50, width = (self.span),fg_color="white", bg_color=theme)
        self.expenseFrame.grid(row = 6, column = 0, columnspan = 3, sticky = "nsew")
        for i, name in enumerate(self.expenseName):
            self.expenseLabel1 = CTkLabel(self.expenseFrame, corner_radius=0, text = f"{name[0]}:", text_color="black",font=CTkFont(family = "bookman", size=35, weight="bold"))
            self.expenseLabel1.grid(row = i, column = 0, padx = 20)
        for x, money in enumerate(self.balance):
            self.expenseLabel2 = CTkLabel(self.expenseFrame, corner_radius=0, text=f"${int(money[0]):,d}", text_color="black",font=CTkFont(family = "bookman", size=35, weight="bold"))
            self.expenseLabel2.grid(row = x, column = 2, padx = (100, 0), sticky = "e")


        # self.myframe = MyFrame(master=self)
        # self.myframe.grid(row=0, column=0, padx = 45)




        
        # CTkLabel(master=self.myframe, text=f" Account balance \n ${'{:.2f}'.format(self.balance)}").grid(row=0, column=0)
        

    
        
        # CTkLabel(master=self.myframe, text=f" Savings balance \n ${'{:.2f}'.format(self.balance)}").grid(row=0, column=1)
        # CTkButton(master=self.myframe, text="Deposit",command=self.addFunds).grid(pady=25, row=1, column=0)
        # CTkButton(master=self.myframe, text="Withdrawl").grid(row=2, column=0)
        # CTkButton(master = self.myframe,text = "Transfer").grid(row= 1, column = 1)
        # self.goals_frame = MyFrame(master=self)
        # self.goals_frame.grid(row=0, column=1)
        # CTkLabel(master=self.goals_frame, text="Enter your goals:").grid(row=0, column=0)
        # self.goals_entry = CTkEntry(master=self.goals_frame)
        # self.goals_entry.grid(row=1, column=0)
        # CTkButton(master=self.goals_frame, text="Add Goal", command=self.save_goals).grid(row=2, column=0)
        
        # self.load_goals(user)
        
        # Retrieve expenses from the database'''
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        expenses = cursor.execute(f"SELECT expense FROM expenses WHERE username = '{self.user}';").fetchall()
        
        connection.close()
        # Format and display expenses
        CTkLabel(master=self.myframe, text=f"Expenses: \n").grid(pady = 25, row=4, column=0)
        for i , expense in enumerate(expenses, 4):
            CTkLabel(master = self.myframe, text = f"{expense}").grid(row = i, column = 0)'''
          

        
   
        
        
    def save_goals(self):
        goal = self.goals_entry.get()
        if goal:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO user_goals (username, goal) VALUES (?, ?)", (self.user, goal))
            connection.commit()
            connection.close()
            self.load_goals(self.user)
            self.goals_entry.delete(0, 'end')
        
    def load_goals(self, user):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        goals = cursor.execute(f"SELECT goal FROM user_goals WHERE username = '{user}';").fetchall()
        connection.close()
        for i, goal in enumerate(goals):
            CTkLabel(master=self.goals_frame, text=f"{i+1}. {goal[0]}").grid(row=i+3, column=0)

    def addFunds(self):
        win = CTkToplevel(self)
        win.geometry("300x300")
        
        CTkLabel(master = win, text = "How much would you like to deposit? ").pack()
        deposit = CTkEntry(master = win)
        deposit.pack()
        
        
        def help():
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()    
            amount = deposit.get()
            current_balance = cursor.execute(f"SELECT accountBalance FROM userInfo WHERE username = '{self.user}").fetchone()
            new_balance = current_balance+amount
            cursor.execute(f"UPDATE userInfo SET accountBalance = {new_balance} WHERE username = '{self.user}';")
            connection.close()
            
        CTkButton(master = win , text = "Deposit", command = help).pack()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        self.balance = cursor.execute(f"SELECT accountBalance FROM userInfo WHERE username = '{self.user}';")
        self.balance = cursor.fetchone()[0]
        
        CTkLabel(master=self.myframe, text=f" Account balance \n ${'{:.2f}'.format(self.balance)}").grid(row=0, column=0)
        
        connection.close()

        #Hello 