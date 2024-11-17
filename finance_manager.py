from tkinter import *
from tkinter import messagebox
import new_user_window
import main_program_window
import utils


root_login_interface = Tk()
root_login_interface.title("Log in")
utils.center_window(root_login_interface, 235, 75)

Label(root_login_interface, text="Username: ").grid(row=0, column=0)
input_username = Entry(root_login_interface, borderwidth=2)
input_username.grid(row=0, column=1, columnspan=1)

Label(root_login_interface, text="Password: ").grid(row=1, column=0)
input_password = Entry(root_login_interface, show="*", borderwidth=2)
input_password.grid(row=1, column=1, columnspan=1)

Button(root_login_interface, text = "Login", command=lambda: login_click(input_username.get(), input_password.get())).grid(row=2, column=2)
Button(root_login_interface, text = "Close", command=root_login_interface.destroy).grid(row=2, column=0)
Button(root_login_interface, text = "New user", command=new_user_window.new_user_click).grid(row=2, column=1)


def login_click(username, password):
    if utils.check_login(username, password):
        messagebox.showinfo("Login", "Login successful!")
        root_login_interface.destroy()
        user_id = utils.get_user_id(username)
        main_program_window.open_main_interface(user_id)
    else:
        messagebox.showinfo("Oops!", "Either the username or password is wrong, try again!")

root_login_interface.mainloop()

def new_user_click():
    root_new_user = Tk()
    root_new_user.title("New user")
    utils.center_window(root_new_user, 195, 90)

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
        if utils.check_user_credentials(username, password, email):
            utils.create_user(username, password, email)
        else:
            root_new_user.attributes('-topmost', True)



