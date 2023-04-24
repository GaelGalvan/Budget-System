import tkinter as tk
import sqlite3
from tkinter import ttk

# Database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              first_name TEXT,
              last_name TEXT,
              age INTEGER,
              pronouns TEXT,
              email TEXT,
              subscription_name TEXT,
              subscription_price INTEGER,
              expense_name TEXT,
              expense_price INTEGER,
              monthly_income INTEGER,
              bank_balance INTEGER,
              username TEXT,
              password TEXT)''')

# Window
root = tk.Tk()
root.geometry("703x550")

# Window title
root.title("Budgeteer")

# Tab control
tabControl = ttk.Notebook(root)

# Three tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

# Tab control to each tab
tabControl.add(tab1, text='Home')
tabControl.add(tab2, text='About')
tabControl.add(tab3, text='Contact')

# Style object for tabs
style = ttk.Style()
style.theme_use('default')

# Background color of tabs
style.configure('TFrame', background="Sky blue")
style.map('TFrame', background=[('selected', 'light blue')])

# Selected tab color
style.configure('TNotebook.Tab', background='#F27D42', padding=[82, 5], font=('Arial', 16, 'bold'), foreground='black')
style.map('TNotebook.Tab', background=[("selected", "light blue")])

# Packing tab control into tkinter window
tabControl.pack(expand=1, fill="both")

# Needs to be on another file
# Functions for new pages
def open_registrationPage():
    def register_user():
        # Input values
        first_name = first_entry.get()
        last_name = last_entry.get()
        age = int(age_entry.get())
        pronouns = pro_entry.get()
        email = email_entry.get()
        subscription_name = name_entry.get()
        subscription_price = int(price_entry.get())
        expense_name = exName_entry.get()
        expense_price = int(exPrice_entry.get())
        monthly_income = int(income_entry.get())
        bank_balance = int(balance_entry.get())
        username = username_entry.get()
        password = password_entry.get()

        # Inserting to database
        c.execute('''INSERT INTO users
                     (first_name, last_name, age, pronouns, email, subscription_name, subscription_price,
                      expense_name, expense_price, monthly_income, bank_balance, username, password)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (first_name, last_name, age, pronouns, email, subscription_name, subscription_price,
                   expense_name, expense_price, monthly_income, bank_balance, username, password))

        conn.commit()
        conn.close()
        # Close window
        new_window.destroy()

    new_window = tk.Toplevel(root)
    new_window.geometry("847x650")
    new_window.title("Registration Page")

    # Create tab control
    tabControl = ttk.Notebook(new_window)

    # Three tabs
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    # Tab control to each tab
    tabControl.add(tab1, text='Personal Info')
    tabControl.add(tab2, text='Profile Info')
    tabControl.add(tab3, text='Login Info')

    # Personal info tab
    first_label = tk.Label(tab1, text="First Name")
    first_label.pack(pady=10)
    first_entry = tk.Entry(tab1)
    first_entry.pack(pady=5)

    last_label = tk.Label(tab1, text="Last Name")
    last_label.pack(pady=10)
    last_entry = tk.Entry(tab1)
    last_entry.pack(pady=5)

    age_label = tk.Label(tab1, text="Age")
    age_label.pack(pady=10)
    age_entry = tk.Entry(tab1)
    age_entry.pack(pady=5)

    pro_label = tk.Label(tab1, text="Pronouns")
    pro_label.pack(pady=10)
    pro_entry = tk.Entry(tab1)
    pro_entry.pack(pady=5)

    email_label = tk.Label(tab1, text="Email")
    email_label.pack(pady=10)
    email_entry = tk.Entry(tab1)
    email_entry.pack(pady=5)

    # Profile info tab
    name_label = tk.Label(tab2, text="Name of subscription")
    name_label.pack(pady=10)
    name_entry = tk.Entry(tab2)
    name_entry.pack(pady=5)

    price_label = tk.Label(tab2, text="Price of subscription per month")
    price_label.pack(pady=10)
    price_entry = tk.Entry(tab2)
    price_entry.pack(pady=5)

    add_button = tk.Button(tab2, text="Add subscription ", bg="#F27D42", font=("Arial", 16))
    add_button.pack(pady=15)

    exName_label = tk.Label(tab2, text="Name of expense")
    exName_label.pack(pady=10)
    exName_entry = tk.Entry(tab2)
    exName_entry.pack(pady=5)

    exPrice_label = tk.Label(tab2, text="Price of expense per month")
    exPrice_label.pack(pady=10)
    exPrice_entry = tk.Entry(tab2)
    exPrice_entry.pack(pady=5)

    income_label = tk.Label(tab2, text="Monthly income")
    income_label.pack(pady=10)
    income_entry = tk.Entry(tab2)
    income_entry.pack(pady=5)

    balance_label = tk.Label(tab2, text="Current bank balance")
    balance_label.pack(pady=10)
    balance_entry = tk.Entry(tab2)
    balance_entry.pack(pady=5)

    # Login info tab
    username_label = tk.Label(tab3, text="Username")
    username_label.pack(pady=10)
    username_entry = tk.Entry(tab3)
    username_entry.pack(pady=5)

    password_label = tk.Label(tab3, text="Password")
    password_label.pack(pady=10)
    password_entry = tk.Entry(tab3, show="*")
    password_entry.pack(pady=5)

    confirm_label = tk.Label(tab3, text="Confirm Password")
    confirm_label.pack(pady=10)
    confirm_entry = tk.Entry(tab3, show="*")
    confirm_entry.pack(pady=5)

    # Add tab control to window
    tabControl.pack(expand=1, fill="both")

    # Submit button
    submit_button = tk.Button(new_window, command=register_user, text="Register", bg="#F27D42", font=("Arial", 16), height=2, width=15)
    submit_button.pack(pady=20)




def open_loginPage():
    new_window = tk.Toplevel(root)
    new_window.geometry("800x400")
    new_window.title("Login Page")

    new_label = tk.Label(new_window, text="This is where you login!")
    new_label.pack(pady=50)


# First tab message
welcome_label = tk.Label(tab1, text="Welcome to Budgeteer!", font=("Helvetica", 24), background="Sky blue")
welcome_label.pack(pady=40)

# Register button
open_button = tk.Button(tab1, text="Register", command=open_registrationPage, bg="#F27D42", font=("Arial", 16), height=2, width=15)
open_button.pack(pady=15)

# Login button
open_button2 = tk.Button(tab1, text="Login", command=open_loginPage, bg="#F27D42", font=("Arial", 16), height=2, width=15)
open_button2.pack(pady=15)

# Second tab message
welcome_label = tk.Label(tab2, text="About Us", font=("Helvetica", 24), background="Sky blue")
welcome_label.pack(pady=40)

# Third tab message
welcome_label = tk.Label(tab3, text="Contact Us", font=("Helvetica", 24), background="Sky blue")
welcome_label.pack(pady=40)

# Event loop
root.mainloop()