class Car: #created class
        def __init__(self, brand, model): #parameters passed by user when created object
            self.__brand = brand #class variables
            self.model = model #class variables
            
        def get_brand(self):
            return self.__brand +" !"
            
        def fullname(self):
            return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
            
            
tesla = ElectricCar("Tesla","Model S", "85kWh")
#print(tesla.brand)
print(tesla.get_brand())
# print(tesla.model)
# print(tesla.battery_size)
            

# my_car = Car("Honda","City") #object 
# print(my_car.brand) #print function for model
# print(my_car.model) #print function for model
# print(my_car.fullname())


# my_new_car = Car("Mahindra","XUV")
# print(my_new_car.brand)
# print(my_new_car.model) 
# print(my_new_car.fullname())