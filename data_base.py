import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


def create_connection():
    try:
        load_dotenv()
        connection = mysql.connector.connect(
            host = os.getenv("HOST"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            database = os.getenv("DATABASE")
            )
        print("Established connection")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

