class Car: #created class
    def __init__(self, brand, model): #parameters passed by user when created object
        self.brand = brand #class variables
        self.model = model #class variables
        
    def fullname(self):
        return f"{self.brand} {self.model}"

my_car = Car("Honda","City") #object 
print(my_car.brand) #print function for model
print(my_car.model) #print function for model
print(my_car.fullname())

my_new_car = Car("Mahindra","XUV")

print(my_new_car.brand)
print(my_new_car.model) 
print(my_new_car.fullname())