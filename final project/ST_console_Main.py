"""Oliver Rothe
still couldnt come up with a 'big project' idea so I made
this to fulfill some remaining criteria for the final project.
Features inheritance of classes, GUI, functional decomposition,
input validation, and organized design.

The program is a little gui that allows you to fiddle with a warp core from Star Trek,
the component names are lore accurate, however their functional relationships are not
for the purpose of this project."""

import tkinter as tk
import ST_classes as ST

def main():
    console = ST.UI()
    console.run()

if __name__ == "__main__":
    main()