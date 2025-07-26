import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext


def create_temp_male_component(root_):
    email_status_frame = tk.LabelFrame(root_, text="Temporary Email Status", padx=10, pady=10)
    email_status_frame.place(x=20, y=420, width=550, height=200)

    tk.Label(email_status_frame, text="john.doe@temp-mail.org     ✅ Email verified", fg="green").pack(anchor="w", pady=2)
    tk.Label(email_status_frame, text="anna.smith@temp-mail.org   ⏳ Waiting activation", fg="orange").pack(anchor="w", pady=2)


