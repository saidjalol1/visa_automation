import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext




def create_log_frame(root_):
    log_frame = tk.LabelFrame(root_, text="Logs", padx=10, pady=10)
    log_frame.place(x=600, y=200, width=580, height=420)

    log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD)
    log_text.pack(expand=True, fill="both")

    def log_callback(message):
        log_text.insert(tk.END, f"{message}\n")
        log_text.see(tk.END)  # Auto-scroll

    return log_callback
