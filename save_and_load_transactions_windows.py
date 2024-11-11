import utils
from utils import center_window
from tkinter import *

def save_transaction_window(user_id):
    root_save_transaction = Tk()
    root_save_transaction.title("Save transaction")
    center_window(root_save_transaction, 400, 400)

    Label(root_save_transaction, text="Category: ").grid(row=0, column=0)
    category_info = Entry(root_save_transaction, borderwidth=2, width=40)
    category_info.grid(row=0, column=1)

    Label(root_save_transaction, text="Amount: ").grid(row=1, column=0)
    amount = Entry(root_save_transaction, borderwidth=2, width=40)
    amount.grid(row=1, column=1)

    Label(root_save_transaction, text="Date: ").grid(row=2, column=0)
    date = Entry(root_save_transaction, borderwidth=2, width=40)
    date.grid(row=2, column=1)

    Label(root_save_transaction, text="Description: ").grid(row=3, column=0)
    description = Entry(root_save_transaction, borderwidth=2, width=40)
    description.grid(row=3, column=1)

    Button(root_save_transaction, text="Save", command=lambda:utils.save_transaction(user_id, find_category_id(category_info.get()), amount.get(), description.get(), date.get())).grid(row=4, column=1)


def find_category_id(category):

    match category.lower():
        case "food":
            return 1
        case "bills":
            return 2
        case "fun":
            return 3