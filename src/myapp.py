import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

import logging
import time
import os
import threading
import concurrent.futures

class MyApp():
    def __init__(self,root):
        self.root_window = root
        self.root_window.title("ML Multi Units")
        self.root_window.option_add("*tearOff", False) # This is always a good idea
        self.root_window.protocol("WM_DELETE_WINDOW",self.close_window)

        self.version = "1.0.0"


        self.vers_text = ttk.Label(text=f"VERSION {self.version}")
        self.vers_text.pack(padx=10,pady=10)

        sizegrip = ttk.Sizegrip(self.root_window)
        sizegrip.pack(anchor="s",side="right")

        # Center the window, and set minsize
        self.root_window.update()
        self.root_window.minsize(self.root_window.winfo_width(), self.root_window.winfo_height())
        # x_cordinate = int((self.root_window.winfo_screenwidth()/2) - (self.root_window.winfo_width()/2))
        # y_cordinate = int((self.root_window.winfo_screenheight()/2) - (self.root_window.winfo_height()/2))
        self.root_window.geometry("300x300")
        
        self.root_window.mainloop()

    def close_window(self):
        self.root_window.destroy()

if __name__ == '__main__':
    format = "%(asctime)s.%(msecs)04d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    app = MyApp(tk.Tk())