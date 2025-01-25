class Car: #created class
    def __init__(self, brand, model): #parameters passed by user when created object
        self.brand = brand #class variables
        self.model = model #class variables

my_car = Car("Honda","City") #object 
print(my_car.brand) #print function for model
print(my_car.model) #print function for model