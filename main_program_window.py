from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import dates as mdates
import save_and_load_transactions_windows
from utils import center_window, check_if_category_exist, fetch_data_for_plot
from tkinter import *

def open_main_interface(user_id):
    from create_category_window import create_category_window
    root_main_interface = Tk()
    root_main_interface.title("Finance Manager")
    center_window(root_main_interface, 800, 500)

    Label(root_main_interface, text="Select what you want to do:").grid(row=0, column=0)
    Button(root_main_interface, text="Save a transaction", command=lambda:save_a_transaction_button()).grid(row=1, column=0)
    Button(root_main_interface, text="Create a category", command=lambda:create_a_category_button()).grid(row=2, column=0)

    data  = fetch_data_for_plot(user_id)
    x_data = [datetime.strptime(str(item["transaction_date"]), '%Y-%m-%d').date() for item in data]
    y_data = [item["amount"] for item in data]

    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, marker='o')
    ax.set_title("Recent expenses")
    ax.set_xlabel("Date")
    ax.set_ylabel("Amount")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    fig.autofmt_xdate()

    canvas = FigureCanvasTkAgg(fig, master=root_main_interface)
    canvas.draw()
    canvas.get_tk_widget().place(x=150, y=0)

    def save_a_transaction_button():
        root_main_interface.destroy()
        save_and_load_transactions_windows.save_transaction_window(user_id)

    def create_a_category_button():
        root_main_interface.destroy()
        create_category_window(user_id)


    root_main_interface.mainloop()