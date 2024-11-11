import save_and_load_transactions_windows
import utils
from utils import center_window
from tkinter import *

def open_main_interface(user_id):
    root_main_interface = Tk()
    root_main_interface.title("Finance Manager")
    center_window(root_main_interface, 400, 400)

    Label(root_main_interface, text="Select what you want to do:").grid(row=0, column=0)
    Button(root_main_interface, text="Save a transaction", command=lambda:save_and_load_transactions_windows.save_transaction_window(user_id)).grid(row=1, column=0)


