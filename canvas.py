import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

canvas = tk.Canvas(master=root, bg="lightblue")
canvas.pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(master=root, text="Change color")
#button1.grid(column=0, row=0)
button1.pack(fill=tk.BOTH, expand=True)

root.mainloop()