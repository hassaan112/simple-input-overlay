import tkinter as tk


running = True

def on_closing(stray_icon=None):
        global running
        if stray_icon:
            stray_icon.stop()
        running = False

def root_setup(stray_icon):
    root = tk.Tk()
    root.overrideredirect(True) # This line removes the title bar
    root.geometry("1400x300") # Set window size (optional)
    transparency = 0.7

    root.attributes('-alpha', transparency)
    root.attributes('-transparentcolor', 'pink')
    root.config(bg='pink')
    root.attributes("-topmost", True)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(stray_icon))

    return root

import time
class Timer():
    def __init__(self):
        self.time_start = time.time()
        self.iterations = 0
    
    def update(self):
        self.iterations += 1
        if time.time() - self.time_start >= 1:
            print(self.iterations)
            self.time_start = time.time()
            self.iterations = 0