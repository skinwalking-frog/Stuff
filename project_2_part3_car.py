'''
Project 1 
9/28/23
Travis Santos

Description: A simple program designed to start, and drive an imaginary car.
Now with secret dolphin option! -Oliver Rothe
'''
import time

class Car:
    def __init__(self, gear, engine, name = "Shitbox"):
        self.gear = gear
        self.engine = engine
        self.name = name
        self.dolphin = False

    def mainMenu(self):
        print('\n')
        print('Main Menu\n')
        print('------------------------------------')
        print(f"car name: {self.name}")
        print(f'Engine Status: {self.engine}')
        print(f'Transmission Status: {self.gear}')
        print('------------------------------------')
        print('What would you like to do?\n\n')
        choice = input('(T)urn the key, (S)hift gears, (D)rive, (I)nfo on your current car, or (G)et out of the car, never to return...: (anything else) Drive a dolphin, like from the ocean...')
        choice = choice.upper()
        if choice == 'T':
            if self.engine == 'ON':
                print('You turn the key to the of position, and stop the engine. ')
                self.engine = 'OFF'
                exitChoice = input('Would you like to get out of the car? (Y)es / (N)o: ')
                exitChoice = exitChoice.upper()
                if exitChoice == 'Y':
                    print('You open the door, and get out of the car...Goodbye')
                elif exitChoice == 'N':
                    input('Press any button to continue...')
                    self.mainMenu()
                self.mainMenu()
            elif self.engine == 'OFF':
                print('You turn the key to the on position, and start the engine.')
                self.engine = 'ON'
                driveChoice = input('Would you like change gears, and drive? (Y)es / (N)o: ')
                driveChoice = driveChoice.upper()
                if driveChoice == 'Y':
                    self.trans(self.gear)
                elif driveChoice == 'N':
                    self.mainMenu()
        if choice == 'S':
            self.trans(self.gear)
        if choice == 'D':
            self.drive()
            if choice == 'I':
                self.displayInfo()
        if choice == 'G':
            print('You get out, never to return. Goodbye')
        else:
            self.dolphin = True

    def drive(self):
        if self.engine == 'OFF':
            print('The engine is currently off, and can\'t be driven. ')
            time.sleep(2)
            self.mainMenu()
        elif self.engine == 'ON':
            if self.gear == 'D':
                driveChoice = input('Do you want to start driving? (Y)es / (N)o: ')
                driveChoice = driveChoice.upper()
                if driveChoice == 'Y':
                    print("You start driving")
                    time.sleep(3)
                    print('You keep driving')
                    time.sleep(2)
                    keepDChoice = input('Keep driving? (Y)es / (N)o: ')
                    keepDChoice = keepDChoice.upper()
                    if keepDChoice == 'Y':
                        print('You continue driving forever and never stop')
                    elif keepDChoice == 'N':
                        print('\n\n')
                        print('You stop driving.')
                        time.sleep(2)
                        self.mainMenu()
                elif driveChoice == 'N':
                    self.mainMenu()
            elif self.gear == 'R':
                print('You start driving backwards, you hit a tree. That\'s it. ')
            elif self.gear == 'N':
                print('Your engine starts revving because you\'re in neutral. Your engine explodes. That\'s it. ')
                time.sleep(2)
                self.mainMenu()
            else:
                print('Either you selected something that wasn\'t an existing gear, or you\'re in park.')
                time.sleep(2)
                self.mainMenu()

    def trans(self, gear): #Trans is short for transmission
        self.gear = input(f'You are currently in {gear}\n\nWhat gear would you like to put it in? (P)ark, (R)everse, (N)uetral, (D)rive: ')
        self.gear = self.gear.upper()
        if self.gear == 'P':
            print('You have put the car in Park.\n')
            input('Press any button to continue...')
            self.drive()
        elif self.gear == 'R':
            print('You have put the car in Reverse.\n')
            input('Press any button to continue...')
            self.drive()
        elif self.gear == 'N':
            print('You have put the car in neutral.\n')
            input('Press any button to continue...')
            self.drive()
        elif self.gear == 'D':
            print('You have put the car in Drive.\n')
            input('press any key to continue...')
            self.drive()
        else: 
            print('Only enter a gear to drive. ')
            self.trans(self.gear)
    
    def displayInfo(self):
        print('\n')
        print('---------------------------------------------')
        print('Information about the car you are driving ')
        print('model', self.name)
        print('Style', 'Coupe')
        print('Doors:', '2')
        print('Engine', '1.6 L')
        print('Transmission', '8 Speed Automatic')
        print('---------------------------------------------')

        input('Press any key to continue...')
        self.mainMenu()

my_car = Car('P', 'OFF')

# my_car.drive(my_car.engine, my_car.gear)
# my_car.trans('P')

my_car.mainMenu()

if my_car.dolphin == True:
    with open("dolphin.txt") as file:
        car_name = file.readline()
        car_eng = file.readline()
        car_trans = file.readline()
        dolphin = Car(car_trans, car_eng, car_name)
    dolphin.mainMenu()
else:
    print("you got your head bitten off by a wild flying dolphin while walking away from your car")