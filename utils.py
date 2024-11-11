import re
from tkinter import messagebox
import bcrypt
from dataBase import create_connection
import pandas as pd

def create_user(username, password, email):
    connection = create_connection()
    hashed_password = hash_password(password)
    query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    values = (username, hashed_password, email)

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    print("New user has been created!")

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(hashed_password, password):
    return bcrypt.checkpw(password.encode(), hashed_password)

def get_transactions(user_id):
    connection = create_connection()
    query = "SELECT * FROM transactions WHERE user_id = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    connection.close()

    dataframe = pd.DataFrame(rows)
    return dataframe

def check_login(username, password):
    connection = create_connection()
    query = "SELECT password FROM users WHERE username = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (username,))
    rows = cursor.fetchall()
    connection.close()
    dataframe = pd.DataFrame(rows)
    hashed_password = dataframe['password'].iloc[0].encode('utf-8')

    return check_password(hashed_password, password)

def check_if_username_exist(username):
    connection = create_connection()
    query = "SELECT 1 FROM users WHERE username = %s LIMIT 1;"
    cursor = connection.cursor()
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False


def check_if_email_exist(email):
    connection = create_connection()
    query = "SELECT 1 FROM users WHERE email = %s LIMIT 1;"
    cursor = connection.cursor()
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False

def test_password(password):
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password):
        return True

def test_email(email):
    if re.search(r'@, \.', email):
        return True

def check_user_credentials(username, password, email):
    if check_if_username_exist(username):
        messagebox.showinfo("Oops!", "Username already exists!")
        return False
    elif check_if_email_exist(email):
        messagebox.showinfo("Oops!", "We have already registered an account for this e-mail!")
        return False
    elif len(password) <= 11:
        messagebox.showinfo("Oops!", "Password is too short. Must contain 12 or more characters!")
        return False
    elif not test_password(password):
        messagebox.showinfo("Oops!", "Password needs to contain at least one uppercase, one lowercase, and one number!")
        return False
    elif not test_email(email):
        messagebox.showinfo("Oops!", "Please enter a valid e-mail address!")
    else:
        return True
