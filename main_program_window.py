from utils import center_window
from tkinter import *

def open_main_interface():
    root_main_interface = Tk()
    root_main_interface.title("Finance Manager")
    center_window(root_main_interface, 400, 400)

    Label(root_main_interface, text="Select what you want to do:").grid(row=0, column=0)
    Button(root_main_interface, text="Save a transaction").grid(row=1, column=0)

