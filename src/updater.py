import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

import logging
import time
import os
import threading
import concurrent.futures

class Updater():
    def __init__(self,root,installed_version=None,latest_version=None):
        self.root_window = root
        self.root_window.title("ML Multi Units")
        self.root_window.option_add("*tearOff", False) # This is always a good idea
        self.root_window.protocol("WM_DELETE_WINDOW",self.close_window)

        self.installed_version = installed_version
        self.latest_version = latest_version

        self.vers_text = ttk.Label(text=f"Current Version is: {self.installed_version}")
        self.vers_text.pack(padx=10,pady=10)

        self.vers_text = ttk.Label(text=f"Latest Version is: {self.latest_version}")
        self.vers_text.pack(padx=10,pady=10)

        sizegrip = ttk.Sizegrip(self.root_window)
        sizegrip.pack(anchor="s",side="right")

        # Center the window, and set minsize
        self.root_window.update()
        self.root_window.minsize(self.root_window.winfo_width(), self.root_window.winfo_height())
        # x_cordinate = int((self.root_window.winfo_screenwidth()/2) - (self.root_window.winfo_width()/2))
        # y_cordinate = int((self.root_window.winfo_screenheight()/2) - (self.root_window.winfo_height()/2))
        self.root_window.geometry("300x100")
        
        self.root_window.mainloop()

    def close_window(self):
        self.root_window.destroy()

def start():
    app = Updater(tk.Tk())