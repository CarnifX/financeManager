import utils
from create_category_window import create_category_window
from data_base import create_connection
from utils import center_window, create_new_category
from tkinter import *

def save_transaction_window(user_id):
    root_save_transaction = Tk()
    root_save_transaction.title("Save transaction")
    center_window(root_save_transaction, 320, 115)

    Label(root_save_transaction, text="Category: ").grid(row=0, column=0)
    category_name = Entry(root_save_transaction, borderwidth=2, width=40)
    category_name.grid(row=0, column=1, columnspan=4)

    Label(root_save_transaction, text="Amount: ").grid(row=1, column=0)
    amount = Entry(root_save_transaction, borderwidth=2, width=40)
    amount.grid(row=1, column=1, columnspan=4)

    Label(root_save_transaction, text="Date: ").grid(row=2, column=0)
    date = Entry(root_save_transaction, borderwidth=2, width=40)
    date.grid(row=2, column=1, columnspan=4)

    Label(root_save_transaction, text="Description: ").grid(row=3, column=0)
    description = Entry(root_save_transaction, borderwidth=2, width=40)
    description.grid(row=3, column=1, columnspan=4)

    Button(root_save_transaction, text="Cancel", command=root_save_transaction.destroy).grid(row=4, column=1)
    Button(root_save_transaction, text="Save", command=lambda:(save_transaction(find_category_id()))).grid(row=4, column=3)

    def find_category_id():
        if utils.check_if_category_exist(category_name):
            return utils.get_category_id(category_name)
        else:
            root_want_new_category = Tk()
            root_want_new_category.title("Create new category?")
            center_window(root_want_new_category, 180, 65)

            Label(root_want_new_category, text="We can't find the category. \n Do you want to create a new one?").grid(
                row=0, column=0, columnspan=10)
            Button(root_want_new_category, text="No", command=root_want_new_category.destroy, width=12).grid(row=1,
                                                                                                             column=1)
            Button(root_want_new_category, text="Yes",
                   command=lambda: (root_want_new_category.destroy(), create_category_window(user_id)), width=12).grid(
                row=1, column=4)


    def save_transaction(category_id):
        from main_program_window import open_main_interface
        connection = create_connection()
        query = "INSERT INTO transactions (user_id, category_id, amount, description, transaction_date) VALUES (%s, %s, %s, %s, %s)"
        values = (user_id, category_id, amount, description, date)

        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        print("The transaction is now logged!")
        root_save_transaction.destroy()
        open_main_interface(user_id)



