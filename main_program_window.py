import save_and_load_transactions_windows
from utils import center_window, check_if_category_exist
from tkinter import *

def open_main_interface(user_id):
    from create_category_window import create_category_window
    root_main_interface = Tk()
    root_main_interface.title("Finance Manager")
    center_window(root_main_interface, 400, 400)

    Label(root_main_interface, text="Select what you want to do:").grid(row=0, column=0)
    Button(root_main_interface, text="Save a transaction", command=lambda:save_and_load_transactions_windows.save_transaction_window(user_id)).grid(row=1, column=0)
    Button(root_main_interface, text="Create a category", command=lambda:create_category_window(user_id)).grid(row=2, column=0)

    root_main_interface.mainloop()

