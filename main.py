import tkinter as tk
import time

root = tk.Tk()
root.overrideredirect(True) # This line removes the title bar
root.geometry("400x300") # Set window size (optional)

# Add your widgets here, e.g., buttons, labels, etc.
# labels = [tk.Label(root, text="bingus"), tk.Label(root, text="bongos")]
# for label in labels:
#     label.grid()

# Add an opaque frame
frame = tk.Frame(root, bg='white', bd=2, relief='solid')
frame.place(x=50, y=50, width=300, height=200)

# Put some content inside
label = tk.Label(frame, text="Solid Box!", bg='white', font=("Arial", 16))
label.pack(pady=20)



running = True

def on_closing():
    global running
    running = False

root.attributes('-transparentcolor', 'pink')
root.config(bg='pink')
root.protocol("WM_DELETE_WINDOW", on_closing)


def main():
    global running
    
    while running:
        root.update()
        root.update_idletasks()
        time.sleep(0.1)

main()