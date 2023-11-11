import tkinter as tk

class search_GUI():
    def __init__(self):
        self.cwidth = 900
        self.cheight = 500
        self.window = tk.Tk()
        self.window.geometry("1000x600")
        self.window.minsize(1000,600)
        self.window.title("search visual")
        self.window.bind("<Configure>", self.resize_canvas) #call function to resize canvas elements on window resize

        self.canv = tk.Canvas(self.window, width=self.cwidth, height=self.cheight, bg='#b0bbbf')
        self.F_bottom = tk.Frame(self.window, bg="#81c1d6")
        self.enter = tk.Entry(self.F_bottom)
        self.button = tk.Button(self.F_bottom, text="run search", command=self.reset)
        self.label = tk.Label(self.F_bottom, text="enter value to search for")
        
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=4)
        self.window.grid_rowconfigure(1, weight=0)
        self.canv.grid(column=0, row=0, sticky="NSEW")
        self.F_bottom.grid(column=0, row=1, sticky="NSEW")
        self.F_bottom.grid_rowconfigure(0, weight=1)
        self.label.grid(column=0, row=0, sticky="NSEW")
        self.enter.grid(column=1, row=0, sticky="NSEW")
        self.button.grid(column=2, row=0, sticky="NSEW")

        self.iter = 0

    def start_visual(self, list: list[int]):
        """creates the visualizeation of dataset from external list"""
        self.rectangles=[]
        self.height_by_index = []
        for item in range(len(list)):
            #bunch of math to determine the correct coordinates for rectangles to fit on canvas
            self.rectangles.append(self.canv.create_rectangle((item*self.cwidth/len(list))+1, 
                                                         self.cheight-((self.cheight/100)*list[item]), 
                                                         (item*self.cwidth/len(list))+(self.cwidth/100)-1, 
                                                         self.cheight, 
                                                         fill='yellow'))
            self.height_by_index.append(list[item])
            self.window.update()

    def resize_canvas(self, event):
        """resize elements in canvas when window is resized(called by listener in __itit__)"""
        self.newH = event.height
        self.newW = event.width
        for i in range(len(self.rectangles)):
            self.canv.coords(self.rectangles[i],(i*self.newW/len(self.rectangles)+1),
                             self.newH-((self.newH/100)*self.height_by_index[i]),
                             i*self.newW/len(self.rectangles)+(self.newW/100)-1,
                             self.newH)

    def reset(self):
        for a in range(len(self.rectangles)):
            self.iter = 0
            self.canv.itemconfig(self.rectangles[a], fill = "yellow")
        try:
            self.target = int(self.enter.get())
        except ValueError:
            self.window.quit()
        self.search()

    def search(self):        
        # for i in range(len(self.rectangles)):
        if self.iter >= len(self.rectangles):
            print("search complete")
        elif self.height_by_index[self.iter] != self.target:
            self.canv.itemconfig(self.rectangles[self.iter], fill = "red")
            self.iter+=1
            self.window.after(200, self.search)
        else:
            self.canv.itemconfig(self.rectangles[self.iter], fill = "green")
            self.iter+=1
            self.window.after(200, self.search)        

    def run(self):
        """runs the main loop"""
        self.window.mainloop()

if __name__=="__main__":
    gui = search_GUI()
    gui.run()