import tkinter as tk
import time, keyboard

root = tk.Tk()
root.overrideredirect(True) # This line removes the title bar
root.geometry("400x300") # Set window size (optional)

# Add your widgets here, e.g., buttons, labels, etc.
# labels = [tk.Label(root, text="bingus"), tk.Label(root, text="bongos")]
# for label in labels:
#     label.grid()

# Add an opaque frame
# frame = tk.Frame(root, bg='white', bd=2, relief='solid')
# frame.grid(column=0, sticky="nsew")

# # Put some content inside
# label = tk.Label(frame, text="Solid Box!", bg='white', font=("Arial", 16))
# label.pack(pady=20)


width = 100
height = 100
class Key(tk.Frame):
    def __init__(self, parent, text, column=0, row=0):
        super().__init__(parent, width=100, height=100, bg='white', relief='solid')
        self.parent = parent
        self.grid_propagate(False)
        self.text = text
        self.setup(self.text)
        self.grid(column=column, row=row, padx=2, pady=2)

    def setup(self, text): 
        self.label = tk.Label(self, text=text, bg='white', font=("Arial", 16))
        self.label.place(relx=0.5, rely=0.5, anchor='center')

    def key_pressed(self):
        self["bg"] = "red"
        self.label["bg"] = "red"


keys = {
    "W": Key(root, "W", 1, 0),
    "A": Key(root, "A", 0, 1),
    "S": Key(root, "S", 1, 1),
    "D": Key(root, "D", 2, 1)
}
# key1 = Key(root, "W", 1, 0)
# key2 = Key(root, "A", 0, 1)
# key3 = Key(root, "S", 1, 1)
# key4 = Key(root, "D", 2, 1)

running = True

def on_closing():
    global running
    running = False

transparency = 0.5

root.attributes('-alpha', transparency)
root.attributes('-transparentcolor', 'pink')
root.config(bg='pink')
root.protocol("WM_DELETE_WINDOW", on_closing)


def main():
    global running
    
    while running:
        root.update()
        root.update_idletasks()
        for key in list(keys.keys()):
            if keyboard.is_pressed(key):
                keys[key].key_pressed()

        time.sleep(0.1)

main()