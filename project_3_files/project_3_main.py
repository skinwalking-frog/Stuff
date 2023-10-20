import class_ts as TS
import Classes_OR as OR
import tkinter as TK

#making window
window = TK.Tk()

#creating objects
oven = OR.oven()
tray = OR.baking_sheet()
pizza = TS.Pizza("?","?","?","?","?")

#set basic window parameters
window.title = "Oven program"
window.geometry('900x450')

#define the grid
rows = 3
columns = 2

#array for referencing frames made in loop
frames_array = []

for c in range(0,columns):
    window.columnconfigure(c, weight=1)
    frames_array.append([])
    for r in range(0,rows):
        window.rowconfigure(r, weight=1)
        frame = TK.Frame(master=window, relief=TK.GROOVE)
        frame.grid(column=c, row=r, sticky='nsew')
        
        frames_array[c].append(frame)

#label for oven attributes
oven_label = TK.Label(master=frames_array[0][0], text=(f"OVEN:\n"
                    f"Rack level: {oven.rack}\n"
                    f"Door: {oven.door}\n"
                    f"Temp: {oven.temp}\n"
                    f"Empty: {oven.empty}"), relief=TK.GROOVE)
oven_label.config(font=("Arial", 20))
oven_label.pack(fill=TK.BOTH, expand=True)

#label for baking sheet attributes
Bsheet_label = TK.Label(master=frames_array[0][1], text=f"Baking sheet:\nContents: {tray.load}", relief=TK.GROOVE)
Bsheet_label.config(font=("Arial", 20))
Bsheet_label.pack(fill=TK.BOTH, expand=True)

#label for pizza attributes
Pizza_label = TK.Label(master=frames_array[0][2],
                        text=("Pizza: \n"
                            f"size: {pizza.size}\n"
                            f"shape: {pizza.shape}\n"
                            f"meat: {pizza.meat_type}\n"
                            f"veges: {pizza.veg_type}\n"
                            f"crust: {pizza.crust_type}"), relief=TK.GROOVE)
Pizza_label.config(font=("Arial", 20))
Pizza_label.pack(fill=TK.BOTH, expand=True)


window.mainloop()