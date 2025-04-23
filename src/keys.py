import tkinter as tk
import keyboard

class Key(tk.Frame):
    def __init__(self, parent, text, column=0, row=0, colspan=1, rowspan=1, width=100, height=100):
        super().__init__(parent, width=width, height=height, bg='white', relief='solid')
        self.parent = parent
        self.grid_propagate(False)
        self.text = text
        self.setup(self.text)
        self.grid(column=column, row=row, padx=2, pady=2, columnspan=colspan)

    def setup_key_listeners(self):
        keyboard.on_press_key(self.text, lambda e: self.after(0, self.key_pressed))
        keyboard.on_release_key(self.text, lambda e: self.after(0, self.key_released))

    def setup(self, text): 
        self.label = tk.Label(self, text=text, bg='white', font=("Arial", 16))
        self.label.place(relx=0.5, rely=0.5, anchor='center')
        # keyboard.on_press_key(self.text, lambda e: self.after(0, self.key_pressed))
        # keyboard.on_release_key(self.text, lambda e: self.after(0, self.key_released))

    def key_pressed(self, *e):
        # self["bg"] = "red"
        # self.label["bg"] = "red"
        self.configure(bg="red")
        self.label.configure(bg="red")
    
    def key_released(self, *e):
        # self["bg"] = "white"
        # self.label["bg"] = "white"
        self.configure(bg="white")
        self.label.configure(bg="white")

    def check_pressed(self):
        if keyboard.is_pressed(self.text):
            self["bg"] = "red"
            self.label["bg"] = "red"
        else:
            self.configure(bg="white")
            self.label.configure(bg="white")