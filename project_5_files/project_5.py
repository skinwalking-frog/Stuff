"""
Oliver Rothe
"""
import random
import tkinter as tk
import project_5_GUI as p5
if __name__=="__main__":    
    dataset = []
    for i in range(1,100):
        dataset.append(random.randint(1,100)) #make 100 random values

    GUI = p5.search_GUI()
    GUI.start_visual(dataset)
    GUI.run()

