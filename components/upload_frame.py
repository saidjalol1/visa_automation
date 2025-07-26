import tkinter as tk
from tkinter import filedialog
from utils.excel_reader import read_excel
import asyncio
import threading

def create_upload_component(root_, log_call_back, fram_call_back):
    upload_frame = tk.LabelFrame(root_, text="File Upload", padx=10, pady=10)
    upload_frame.place(x=20, y=80, width=550)

    file_label = tk.Label(upload_frame, text="No file selected")
    file_label.pack(pady=5)

    selected_file = {"path": None}  # Use dict to allow inner function access

    def select_file():
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            selected_file["path"] = file_path
            file_label.config(text=file_path.split("/")[-1])
            data = run_async_in_thread(read_excel(file_path, log_callback=log_call_back,frame_call_back=fram_call_back))
            print(data)

    def run_async_in_thread(coro):
        def runner():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(coro)
            loop.close()
        threading.Thread(target=runner).start()

    tk.Button(upload_frame, text="Select Excel", command=select_file, bg="#1677ff", fg="white").pack(pady=5)
