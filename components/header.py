import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext

def create_header(root_):
    header_frame = tk.Frame(root_, bg="#1677ff", height=60)
    header_frame.pack(fill='x')
    tk.Label(header_frame, text="Visa Appointment Booker", bg="#1677ff", fg="white",
         font=("Arial", 18, "bold")).pack(side="left", padx=20, pady=10)


