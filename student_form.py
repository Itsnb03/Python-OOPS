class Student:
    def __init__(self, rollno, firstname, lastname, course, div,address):
        self.rollno = rollno
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.div = div
        self.address=address
        
    def full_detail(self):
        return f"{self.rollno} {self.firstname} {self.lastname} {self.course} {self.div} {self.address} "
    
class New_admission(Student):
    def __init__(self, rollno, firstname, lastname, course, div, address, gender, dissability):
        super().__init__(rollno, firstname, lastname, course, div, address)
        self.gender = gender
        self.dissability = dissability

std1 = Student("1", "Nitin", "Bharadwaj", "BSCIT", "A", "Borivali")
print(std1.full_detail())
print(std1.rollno)
print(std1.firstname)
print(std1.lastname)
print(std1.course)
print(std1.div)
print(std1.address)

std2 = Student("2", "Aman", "Singh", "BCSIT", "A", "Kandivali")
print(std2.full_detail())
print(std2.rollno)
print(std2.firstname)
print(std2.lastname)
print(std2.course)
print(std2.div)
print(std2.address)

newstd = New_admission("7", "Dev", "Gandhi", "BSCIT", "A", "Dahanu", "Male", "No")
print(newstd.gender)
print(newstd.dissability)