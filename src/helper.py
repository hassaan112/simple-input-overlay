import tkinter as tk
import ctypes
from ctypes import windll


running = True

def on_closing(stray_icon=None):
    global running
    if stray_icon:
        stray_icon.stop()
    running = False

def root_setup(stray_icon):
    root = tk.Tk()
    root.overrideredirect(True) # This line removes the title bar
    root.geometry("400x300") # Set window size (optional)
    root.attributes("-topmost", True)
    transparency = 0.5

    root.attributes('-alpha', transparency)
    root.attributes('-transparentcolor', 'pink')
    root.config(bg='pink')
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(stray_icon))

    # Making root window click-through
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())

    # Constants
    GWL_EXSTYLE = -20
    WS_EX_LAYERED = 0x80000
    WS_EX_TRANSPARENT = 0x20
    WS_EX_NOACTIVATE = 0x08000000

    # Apply styles
    styles = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE,
        styles | WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_NOACTIVATE)
    return root