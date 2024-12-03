from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import dates as mdates
import save_and_load_transactions_windows
from utils import center_window, fetch_date_and_amount, fetch_category_and_amount
from tkinter import *


def open_main_interface(user_id):
    from create_category_window import create_category_window
    root_main_interface = Tk()
    root_main_interface.title("Finance Manager")
    center_window(root_main_interface, 800, 525)

    Label(root_main_interface, text="Select what you want to do:").grid(row=0, column=0)
    Button(root_main_interface, text="Save a transaction", command=lambda:save_a_transaction_button()).grid(row=1, column=0)
    Button(root_main_interface, text="Create a category", command=lambda:create_a_category_button()).grid(row=2, column=0)

    scatter_data  = fetch_date_and_amount(user_id)
    x_scatter_data = [datetime.strptime(str(item["transaction_date"]), '%Y-%m-%d').date() for item in scatter_data]
    y_scatter_data = [item["amount"] for item in scatter_data]

    scatter_fig, scatter_ax = plt.subplots(figsize=(5, 3))
    scatter_ax.scatter(x_scatter_data, y_scatter_data, marker='o')
    scatter_ax.set_title("Recent expenses")
    scatter_ax.set_xlabel("Date")
    scatter_ax.set_ylabel("Amount")
    scatter_ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    scatter_fig.autofmt_xdate()
    scatter_canvas = FigureCanvasTkAgg(scatter_fig, master=root_main_interface)
    scatter_canvas.draw()
    scatter_canvas.get_tk_widget().place(x=150, y=0)

    pie_data = fetch_category_and_amount(user_id)
    data_labels = [item["name"] for item in pie_data]
    data_amount = [item["amount"] for item in pie_data]
    pie_labels, pie_amount = add_list_values(data_amount, data_labels)

    pie_fig, pie_ax = plt.subplots(figsize=(5, 2))
    pie_ax.pie(pie_amount, labels=pie_labels, autopct='%1.1f%%', shadow=True, startangle=90)
    pie_ax.set_title('Expense Distribution')
    pie_canvas = FigureCanvasTkAgg(pie_fig, master=root_main_interface)
    pie_canvas.draw()
    pie_canvas.get_tk_widget().place(x=150, y=325)

    def save_a_transaction_button():
        root_main_interface.destroy()
        save_and_load_transactions_windows.save_transaction_window(user_id)


    def create_a_category_button():
        root_main_interface.destroy()
        create_category_window(user_id)


    root_main_interface.mainloop()

def add_list_values(amounts, names):
    finished_product = {}

    for name, amount in zip(names, amounts):
        if name in finished_product:
            finished_product[name] += amount
        else:
            finished_product[name] = amount

    return list(finished_product.keys()), list(finished_product.values())
