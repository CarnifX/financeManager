from tkinter import *
from tkinter import messagebox
from utils import check_login, create_user, check_user_credentials


def create_user_interface():
    root_login_interface = Tk()
    root_login_interface.title("Log in")
    center_window(root_login_interface, 235, 75)

    Label(root_login_interface, text="Username: ").grid(row=0, column=0)
    input_username = Entry(root_login_interface, borderwidth=2)
    input_username.grid(row=0, column=1, columnspan=1)

    Label(root_login_interface, text="Password: ").grid(row=1, column=0)
    input_password = Entry(root_login_interface, show="*", borderwidth=2)
    input_password.grid(row=1, column=1, columnspan=1)

    Button(root_login_interface, text = "Enter", command=lambda: enter_click(input_username.get(), input_password.get())).grid(row=2, column=2)
    Button(root_login_interface, text = "Close", command=root_login_interface.destroy).grid(row=2, column=0)
    Button(root_login_interface, text = "New user", command=new_user_click).grid(row=2, column=1)

    def enter_click(username, password):
        if check_login(username, password):
            messagebox.showinfo("Login", "Login successful!")
            root_login_interface.destroy()
            open_main_interface()

    root_login_interface.mainloop()

def new_user_click():
    root_new_user = Tk()
    root_new_user.title("New user")
    center_window(root_new_user,195, 90)

    Label(root_new_user, text="Username: ").grid(row=0, column=0, columnspan=2)
    new_username = Entry(root_new_user, borderwidth=2)
    new_username.grid(row=0, column=2, columnspan=2)

    Label(root_new_user, text="Password: ").grid(row=1, column=0, columnspan=2)
    new_password = Entry(root_new_user, show="*", borderwidth=2)
    new_password.grid(row=1, column=2, columnspan=2)

    Label(root_new_user, text="E-mail: ").grid(row=2, column=0, columnspan=2)
    new_email = Entry(root_new_user, borderwidth=2)
    new_email.grid(row=2, column=2, columnspan=2)

    Button(root_new_user, text="Enter", command=lambda: new_user_enter_click(new_username.get(), new_password.get(), new_email.get())).grid(row=3, column=3)
    Button(root_new_user, text="Close", command=root_new_user.destroy).grid(row=3, column=1)

    def new_user_enter_click(username, password, email):
        root_new_user.attributes('-topmost', False)
        if check_user_credentials(username, password, email):
            create_user(username, password, email)
        else:
            root_new_user.attributes('-topmost', True)

def open_main_interface():
    root_main_interface = Tk()
    root_main_interface.title("Finance Manager")
    center_window(root_main_interface, 400, 400)

    Label(root_main_interface, text="Select what you want to do:").grid(row=0, column=0)


def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")