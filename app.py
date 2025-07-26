import os
import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext
from components import header, booking, data_frame, log_frame, upload_frame
from config import DB_FILE



root = tk.Tk()
root.title("Visa Appointment Booker")
root.geometry("1200x700")
root.configure(bg="#f4f4f4")





def on_exit():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)


# eventlar
root.protocol("WM_DELETE_WINDOW", on_exit)

# Components integration
header.create_header(root)
booking.create_booking_component(root)
frame_call_back = data_frame.create_data_preview_component(root)

log_callback = log_frame.create_log_frame(root)
upload_frame.create_upload_component(root, log_callback, fram_call_back=frame_call_back)




root.mainloop()