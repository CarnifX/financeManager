import utils
from create_category_window import create_category_window
from utils import center_window, create_new_category
from tkinter import *

def save_transaction_window(user_id):
    root_save_transaction = Tk()
    root_save_transaction.title("Save transaction")
    center_window(root_save_transaction, 400, 400)

    Label(root_save_transaction, text="Category: ").grid(row=0, column=0)
    category_name = Entry(root_save_transaction, borderwidth=2, width=40)
    category_name.grid(row=0, column=1)

    Label(root_save_transaction, text="Amount: ").grid(row=1, column=0)
    amount = Entry(root_save_transaction, borderwidth=2, width=40)
    amount.grid(row=1, column=1)

    Label(root_save_transaction, text="Date: ").grid(row=2, column=0)
    date = Entry(root_save_transaction, borderwidth=2, width=40)
    date.grid(row=2, column=1)

    Label(root_save_transaction, text="Description: ").grid(row=3, column=0)
    description = Entry(root_save_transaction, borderwidth=2, width=40)
    description.grid(row=3, column=1)


    try:
        Button(root_save_transaction, text="Save", command=lambda:(utils.save_transaction(user_id, find_category_id(category_name.get(), user_id), amount.get(), description.get(), date.get()), root_save_transaction.destroy())).grid(row=4, column=1)
    finally:
        None


def find_category_id(category_name, user_id):
    if utils.check_if_category_exist(category_name):
        return utils.get_category_id(category_name)
    else:
        root_want_new_category = Tk()
        root_want_new_category.title("Create new category?")
        center_window(root_want_new_category, 180,65)

        Label(root_want_new_category, text="We can't find the category. \n Do you want to create a new one?").grid(row=0, column=0, columnspan=10)
        Button(root_want_new_category, text="No", command=root_want_new_category.destroy, width=12).grid(row=1, column=1)
        Button(root_want_new_category, text="Yes", command=lambda:(root_want_new_category.destroy(), create_category_window(user_id)), width=12).grid(row=1, column=4)
