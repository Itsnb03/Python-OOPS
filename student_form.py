class Student:
    def __init__(self, rollno, name,course, div,address):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.div = div
        self.address=address

std1 = Student("4", "Nitin", "BSCIT", "A", "Borivali")
print(std1.rollno)
print(std1.name)
print(std1.course)
print(std1.div)
print(std1.address)

std2 = Student("5", "Aman", "BCSIT", "A", "Kandivali")
print(std2.rollno)
print(std2.name)
print(std2.course)
print(std2.div)
print(std2.address)