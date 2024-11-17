import re
from tkinter import messagebox
import bcrypt
from data_base import create_connection
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

def get_user_id(username):
    connection = create_connection()
    query = "SELECT user_id FROM users WHERE username = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    connection.close()
    user_id = result["user_id"]
    return user_id

def check_login(username, password):
    if check_if_username_exist(username):
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
    cursor.close()
    connection.close()

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
    cursor.close()
    connection.close()

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

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def save_transaction(user_id, category_id, amount, description, date):
    connection = create_connection()
    query = "INSERT INTO transactions (user_id, category_id, amount, description, transaction_date) VALUES (%s, %s, %s, %s, %s)"
    values = (user_id, category_id, amount, description, date)

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    print("The transaction is now logged!")

def create_new_category(category_name, category_type):
    connection = create_connection()
    query = "INSERT INTO categories (name, type) VALUES (%s, %s)"
    values = (category_name, category_type)
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    messagebox.showinfo("Updated!", f"You've successfully added {category_name} to the database!")

def check_if_category_exist(category_name):
    connection = create_connection()
    query = "SELECT 1 FROM categories WHERE name = %s LIMIT 1;"
    cursor = connection.cursor()
    cursor.execute(query, (category_name,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        return True
    else:
        return False

def get_category_id(category_name):
    connection = create_connection()
    query = "SELECT category_id FROM categories WHERE name = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (category_name,))
    result = cursor.fetchone()
    connection.close()
    category_id = result["category_id"]
    return category_id