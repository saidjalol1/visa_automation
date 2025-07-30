import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext


def create_booking_component(root_):
    booking_frame = tk.LabelFrame(root_, text="Booking Automation", padx=10, pady=10)
    booking_frame.place(x=600, y=80, width=580, height=100)

    tk.Button(booking_frame, text="Start Booking", bg="#28a745", fg="white").pack(side="left", padx=10)
    tk.Button(booking_frame, text="Start Registering", bg="#f70909", fg="white").pack(side="left", padx=10)

    progress = ttk.Progressbar(booking_frame, length=560, value=0)
    progress.pack()
    