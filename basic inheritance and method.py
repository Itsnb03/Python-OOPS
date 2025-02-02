# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic sound"

# Child Class 1
class Dog(Animal):
    def sound(self):
        return "Bark"

# Child Class 2
class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating Objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Accessing Methods
print(f"{dog.name} says: {dog.sound()}")  # Output: Buddy says: Bark
print(f"{cat.name} says: {cat.sound()}")  # Output: Whiskers says: Meow
