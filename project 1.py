"""
Project 1
Author: Oliver Rothe
year: 9/27/2023
"""

# class Timemachine():
#     def __init__(self, chamber, button, plug, dial):
#         self.chamber = chamber
#         self.button = button
#         self.plug = plug
#         self.dial = dial

class plug():
    def __init__(self, power_use, plugged_in = False):
        self.power_use = power_use
        self.plugged_in = plugged_in

    def toggle_plug(self):
        self.plugged_in = not self.plugged_in

class chamber():
    def __init__(self, speed, spinning = False, open = False):
        self.speed = speed
        self.spinning = spinning
        self.open = open

class button():
    def __init__(self, state = False):
        self.state = state

    def toggle(self):
        self.state = not self.state

class dial():
    def __init__(self, year):
        self.year = year

    def set_year(self, value):
        self.year = value

def inspect_machine(plugged, power_draw, button_state, dial_year, chamber_open, chamber_speed):
    print(f"-----------------------------------------------------------------------------------\n\
plugged in: {plugged}, power usage rate: {power_draw} watts,\n\
spin cycle on: {button_state}, set year: {dial_year},\n\
Chamber door open: {chamber_open}, chamber speed: {chamber_speed} RPM\n\
-----------------------------------------------------------------------------------\n")

TM_dial = dial(2023)
TM_plug = plug(TM_dial.year * 5280)
TM_button = button()
TM_chamber = chamber(TM_dial.year*1000)
#machine = Timemachine(TM_chamber, TM_button, TM_plug, TM_dial)

def main():
    running = True
    print("you are the newest owner of the time machine 3500-A from amazon.com, it is sitting in your garage.")
    while running:
        user_in = input("what would you like to do with your time machine?\n\
                        Options:\n\
                        'inspect' to inspect the machine\n\
                        'change' to set year\n\
                        'plug' to plug/unplug power cable\n\
                        'Go' to start spin cycle\n\
                        'leave' to walk out of your garage and never return\n")
        
        if user_in.lower().strip() == "inspect":
            inspect_machine(TM_plug.plugged_in, TM_plug.power_use, TM_button.state, TM_dial.year, TM_chamber.open, TM_chamber.speed)
        elif user_in.lower().strip() == "change":
            question = int(input("what year would you like to set (whole numbers only)"))
            TM_dial.set_year(question)
            TM_plug.power_use = TM_dial.year * 5280
            TM_chamber.speed = TM_dial.year * 1000
        elif user_in.lower().strip() == "plug":
            TM_plug.toggle_plug()
            TM_chamber.open = True
        elif user_in.lower().strip() == "go":
            TM_chamber.spinning == True
        elif user_in.lower().strip() == "leave":
            print("Goodbye")
            running = False
        else:
            print("unsupported option, try again")

if __name__ == "__main__":
    main()