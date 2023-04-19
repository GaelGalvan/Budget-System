import sqlite3 
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

    