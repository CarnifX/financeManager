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

