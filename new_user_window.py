from tkinter import *
import utils

def new_user_click():
    root_new_user = Tk()
    root_new_user.title("New user")
    utils.center_window(root_new_user,195, 90)

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


