"""
Oliver rothe
prototype GUI for project 4's data searching algorithm
"""

import tkinter as tk

class GUI_1():
    """basic GUI with button label and text box that updates label
    with text from textbox when button is pressed"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.user_in = tk.StringVar(master=self.root)
        self.label = tk.Label(master=self.root, text="empty")
        self.entry = tk.Entry(master=self.root, textvariable=self.user_in)
        self.button = tk.Button(master=self.root, text="set", command=self.set_lab())
        self.label.pack()
        self.entry.pack()
        self.button.pack()

    def set_lab(self):
        self.label.config(text=self.user_in.get())

    def run_GUI(self):
        self.root.mainloop()

window = GUI_1()

window.run_GUI()