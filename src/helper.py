import tkinter as tk


running = True

def on_closing(stray_icon=None):
        global running
        if stray_icon:
             stray_icon.stop()
        print('ae')
        running = False

def root_setup():
    root = tk.Tk()
    root.overrideredirect(True) # This line removes the title bar
    root.geometry("400x300") # Set window size (optional)
    transparency = 0.5

    root.attributes('-alpha', transparency)
    root.attributes('-transparentcolor', 'pink')
    root.config(bg='pink')
    root.protocol("WM_DELETE_WINDOW", on_closing)
    return root