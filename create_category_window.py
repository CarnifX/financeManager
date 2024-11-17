from tkinter import *
from tkinter import messagebox
import utils

def create_category_window(user_id):
    from main_program_window import open_main_interface
    root_create_category = Tk()
    root_create_category.title("New category")
    utils.center_window(root_create_category, 290, 75)

    Label(root_create_category, text="New category name: ").grid(row=0, column=0)
    category_name = Entry(root_create_category, borderwidth=2)
    category_name.grid(row=0, column=1, columnspan=2)

    Label(root_create_category, text="Select income or expanse: ").grid(row=1, column=0)

    category_type = StringVar()

    Radiobutton(root_create_category, text="Income", variable=category_type, value="income").grid(row=1, column=1)
    Radiobutton(root_create_category, text="Expanse", variable=category_type, value="expense").grid(row=1, column=2)

    enter_button = Button(root_create_category, text="Enter", command=lambda: enter_button_click())
    enter_button.grid(row=2, column=2)
    cancel_button = Button(root_create_category, text="Cancel", command=lambda: cancel_button_click())
    cancel_button.grid(row=2, column=0)

    def enter_button_click():
        if not category_name.get():
            messagebox.showinfo("Oops!", "You can't leave the category name open!")
            root_create_category.destroy()

        elif not utils.check_if_category_exist(category_name.get()):
            match category_type.get():
                case "income":
                    utils.create_new_category(category_name.get(), category_type.get())
                    root_create_category.destroy()
                    open_main_interface(user_id)
                case "expense":
                    utils.create_new_category(category_name.get(), category_type.get())
                    root_create_category.destroy()
                    open_main_interface(user_id)

        else:
            messagebox.showinfo("Oops!", "This category already exists!")
            root_create_category.destroy()

    def cancel_button_click():
        root_create_category.destroy()
        open_main_interface(user_id)

    root_create_category.mainloop()