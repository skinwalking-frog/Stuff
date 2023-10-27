"""
Oliver rothe
prototype GUI #2 for project 4
"""

import tkinter as tk

class GUI_2():
    """ten text boxes and button that sets label to next largest value in text boxes"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.boxs = []
        self.user_in = []
        self.label = tk.Label(master=self.root, text="empty")
        for i in range(10):
            self.user_in.append(tk.StringVar(master=self.root))
            self.boxs.append(tk.Entry(master=self.root, textvariable=self.user_in[i]))
            self.boxs[i].pack()
            

        self.button = tk.Button(master=self.root, text="set", command = self.set_lab)
        self.label.pack()
        self.button.pack()

    def set_lab(self):
        self.label.config(text=self.user_in.get())

    def run_GUI(self):
        self.root.mainloop()

if __name__ == "main":
    window = GUI_2()
    window.run_GUI()