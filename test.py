print("-"*20)
class One_1:
    a=10
    _b=20
    __c=30
    
    def getData(self):
        return
        
class Two_2(One_1):
    pass
class Three_3(Two_2):
    pass
class Four_4(Three_3):
    pass
objFour=Four_4()
objOne=One_1()
print(objFour.a)
print(objFour._b)
print(objOne.__c)

print("end"*20)