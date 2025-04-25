import tkinter as tk
import keyboard
import time


class Key(tk.Frame):
    def __init__(self, parent, text, column=0, row=0, colspan=1, rowspan=1, width=100, height=100):
        super().__init__(parent, width=width, height=height, bg='grey', relief='solid')
        self.parent = parent
        self.grid_propagate(False)
        self.text = text
        self.setup(self.text)
        self.grid(column=column, row=row, padx=2, pady=2, columnspan=colspan)
        self.time = None

    def setup(self, text): 
        self.label = tk.Label(self, text=text, bg='grey', font=("Arial", 16))
        self.label.place(relx=0.5, rely=0.5, anchor='center')

    # def key_pressed(self, *e):
    #     # self["bg"] = "red"
    #     # self.label["bg"] = "red"
    #     self.configure(bg="red")
    #     self.label.configure(bg="red")
    
    # def key_released(self, *e):
    #     # self["bg"] = "white"
    #     # self.label["bg"] = "white"
    #     self.configure(bg="white")
    #     self.label.configure(bg="white")

    def check_pressed(self):
        if keyboard.is_pressed(self.text):
            self["bg"] = "white"
            self.label["bg"] = "white"
            self.label["text"] = self.hold_time()
        else:
            self.time = None
            self.configure(bg="grey")
            self.label.configure(bg="grey")
            self.label.configure(text=self.text)
        
    def pressed(self):
        self["bg"] = "white"
        self.label["bg"] = "white"
        
    def held(self):
        self.label["text"] = self.hold_time()
    
    def released(self):
        self.time = None
        self.configure(bg="grey")
        self.label.configure(bg="grey")
        self.label.configure(text=self.text)

    def hold_time(self):
        if not self.time:
            self.time = time.time()
        return round((time.time() - self.time), 2)