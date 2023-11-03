"""
Oliver rothe
GUI #2 for project 4
"""

import tkinter as tk

class GUI_2():
    """ten text boxes and button that sets label to next smallest value in text boxes"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.boxs = []
        self.user_in = []
        self.label = tk.Label(master=self.root, text="empty")
        for i in range(10):
            self.boxs.append(tk.Entry(master=self.root))
            self.boxs[i].pack()

        self.button = tk.Button(master=self.root, text="next", command = self.set_lab)
        self.label.pack()
        self.button.pack()
        self.root.bind_all('<Key>', self.update_user_in) #update set of input numbers everytime a key is pressed

    def update_user_in(self, event):
        self.user_in = []
        for i in range(len(self.boxs)):
            if self.boxs[i].get() != "":
                self.user_in.append(int(self.boxs[i].get()))

    def set_lab(self):
        if len(self.user_in) >= 1:
            self.user_in.sort()  #is this cheating a little?  
            self.label.config(text=self.user_in.pop(0))

    def run_GUI(self):
        self.root.mainloop()

if __name__ == "__main__":
    window = GUI_2()
    window.run_GUI()

#pytest wont install properly. 
#But some basic tests I could run would be: 
#putting undesired input into the boxes to see if the program crashes. 
#(it does error, because it cant cast alphabetical chars to an int)
#enter numbers in only some boxes. (the program actually still works for this one)
#test individual class methods in an isolated environment to see if they output correctly or if they can handle others types of input.