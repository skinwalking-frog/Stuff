import tkinter as tk

class search_GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1000x600")
        self.window.title("search visual")

        self.canv = tk.Canvas(self.window, width=900, height=400, bg='#b0bbbf')
        self.F_bottom = tk.Frame(self.window, bg="#81c1d6")
        self.enter = tk.Entry(self.F_bottom)
        self.button = tk.Button(self.F_bottom, text="run search")
        self.label = tk.Label(self.F_bottom, text="enter value to search for")
        

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=2)
        self.window.grid_rowconfigure(1, weight=1)
        self.canv.grid(column=0, row=0, sticky="NSEW")
        self.F_bottom.grid(column=0, row=1, sticky="NSEW")



    def run(self):
        self.window.mainloop()

gui = search_GUI()
gui.run()