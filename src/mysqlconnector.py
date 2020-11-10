#Modules

import mysql.connector
from src.config import *

# MySQL connector

mydb = mysql.connector.connect(
  host=hostname,
  user=username,
  database=dbname,
  password=passw
)

# Search function [username]
def mysqlsearch_username():   
    mycursor = mydb.cursor()
    username = input("Username : ")
    sql = "SELECT * FROM accounts WHERE username ='" + username + "'"
    
    mycursor.execute(sql)
    
    myresult = mycursor.fetchall()
    
    for result in myresult:
        print(result)
        
# Search function [email]
def mysqlsearch_email():   
    mycursor = mydb.cursor()
    email = input("Email : ")
    sql = "SELECT * FROM accounts WHERE email ='" + email + "'"
    
    mycursor.execute(sql)
    
    myresult = mycursor.fetchall()
    
    for result in myresult:
        print(result)  
        
# Search function [Password]
def mysqlsearch_password():   
    mycursor = mydb.cursor()
    password = input("Password : ")
    sql = "SELECT * FROM accounts WHERE password ='" + password + "'"
    
    mycursor.execute(sql)
    
    myresult = mycursor.fetchall()
    
    for result in myresult:
        print(result)       
