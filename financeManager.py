import userInterface
from dataBase import create_connection

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


userInterface.create_user_interface()



