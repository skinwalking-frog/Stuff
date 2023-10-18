"""
Oliver Rothe

class objects for project_3_main.py
"""

class oven():
    def __init__(self, level = 1):
        self.rack_level_dict = {1:"top", 2:"middle", 3:"bottom"}
        self.rack = self.rack_level_dict[level]
        self.door = "open"
        self.temp = 0
        self.empty = True

    def door_toggle(self):
        """toggles door open/closed"""

        if self.door == "open":
            self.door = "closed"
        elif self.door =="closed":
            self.door = "open"

    def set_rack(self, level = int):
        """set position of oven rack"""
        self.rack = self.rack_level_dict[level]

    def preheat(self, temperature):
        """set temperature"""
        self.temp = temperature

    def ison(self):
        """check if on"""
        if self.temp > 0:
            return True
        else:
            return False

    def isfull(self):
        """check if full"""
        if self.empty == True:
            return False
        else:
            return True
        
    def toggle_load(self):
        """load/unload oven"""
        self.emtpy = not self.empty


class baking_sheet():
    def __init__(self, size, load):
        self.size = f"{size} square inches"
        self.load = load

    def change_load(self, load):
        self.load = load

