import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext
from config import FILE_PATH
from utils.db_commands import read_from_table

columns = (
    "id", "Category", "SubCategory", "City", "Fullname", "Passport", 
    "Birth_date", "Passport validity", "Gender", "Phone", "Nation", 
    "Book date from", "Book date to", "Email", "Password"
)

def populate_tree(tree):
    """
    Clear and re-populate the Treeview with data from the DB
    """

    for row in tree.get_children():
        tree.delete(row)

    
    rows = read_from_table("users")
    for i in rows:
        tree.insert("", "end", values=i)


def create_data_preview_component(root_):
    preview_frame = tk.LabelFrame(root_, text="Data Preview", padx=10, pady=10)
    preview_frame.place(x=20, y=200, width=550, height=420)

    columns = ("id","Category","SubCategory","City","Fullname", "Passport","Birth_date","Passport validity","Gender","Phone","Nation","Book date from","Book date to","Email","Password")


    container = tk.Frame(preview_frame)
    container.pack(fill="both", expand=True)
    
    
    tree = ttk.Treeview(container, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')


    def call_back():
        rows = read_from_table("users")
        for i in rows:
            tree.insert("", "end", values=i)
    
        
    y_scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
    x_scrollbar = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

 
    tree.grid(row=0, column=0, sticky="nsew")
    y_scrollbar.grid(row=0, column=1, sticky="ns")
    x_scrollbar.grid(row=1, column=0, sticky="ew")

 
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    return call_back



