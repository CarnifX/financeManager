from tkinter import *
import tkinter as tk
from tkinter import messagebox
from utils import check_login, create_user

def create_user_interface():
    root_user_interface = tk.Tk()

    input_username = Entry(root_user_interface)
    input_username.pack()
    input_password = Entry(root_user_interface)
    input_password.pack()

    Button(root_user_interface, text = "Enter", command=lambda: enter_click(input_username.get(), input_password.get())).pack()
    Button(root_user_interface, text = "Close", command=root_user_interface.destroy).pack()
    Button(root_user_interface, text = "Create new user", command=new_user_click).pack()

    def enter_click(username, password):
        if check_login(username, password):
            messagebox.showinfo("Login", "Login successful!")
            root_user_interface.destroy()
            open_main_interface()

    root_user_interface.mainloop()

def new_user_click():
    root_new_user = Tk()
    new_username = Entry(root_new_user)
    new_username.pack()
    new_password = Entry(root_new_user, show="*")
    new_password.pack()
    new_email = Entry(root_new_user)
    new_email.pack()

    Button(root_new_user, text="Enter", command=lambda: new_user_enter_click(new_username.get(), new_password.get(), new_email.get())).pack()
    Button(root_new_user, text="Close", command=root_new_user.destroy).pack()

    def new_user_enter_click(username, password, email):
        create_user(username, password, email)

def open_main_interface():
    root_main_interface = Tk()

    Label(root_main_interface, text="Select what you want to do:").pack()