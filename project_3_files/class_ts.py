class Pizza:
    def __init__(self, size, shape, meat_type, veg_type, crust_type):
        self.size = size,
        self.shape = shape,
        self.meat_type = meat_type,
        self.veg_type = veg_type,
        self.crust_type = crust_type

    def pSize(self, input):
        #1-Small 
        #2-Medium
        #3-Large
        if input == '1':
            self.size = 'small'
        elif input == '2':
            self.size = 'Medium'
        elif input == '3':
            self.size = 'Large'

    def pShape(self, input):
        #1-circle
        #2-square
        #3-Triangle
        #4-Christmas Tree
        if input == '1':
            self.shape = 'Circle'
        elif input == '2':
            self.shape = 'Square'
        elif input == '3':
            self.shape = 'Triangle'
        elif input == '4':
            self.shape = 'Christmas Tree'
    
    
    def pMeatType(self, input):
        #1-Pepperoni
        #2-Sausage
        #3-Chicken
        #4-None
        if input == '1':
            self.meat_type = 'Pepperoni'
        elif input == '2':
            self.meat_type = 'Sausage'
        elif input == '3':
            self.meat_type = 'Chicken'
        elif input == '4':
            self.meat_type = 'None'
    
    def pVegType(self, input):
        #1-Bell Peppers
        #2-Tomatoes
        #3-Olives
        #4-None
        if input == '1':
            self.veg_type = 'Bell Peppers'
        elif input == '2':
            self.veg_type = 'Tomatoes'
        elif input == '3':
            self.veg_type = 'Olives'
        elif input == '4':
            self.veg_type = 'None'

    def pCrustType(self, input):
        #1-Thin
        #2-Thick
        #3-Stuffed
        if input == '1':
            self.crust_type = 'Thin'
        elif input == '2':
            self.crust_type = 'Thick'
        elif input == '3':
            self.crust_type = 'Stuffed'