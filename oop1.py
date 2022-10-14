"""class Student:
    pass

E1= Student()
Mark= Student()
"""

class Employee:
    def __init__(self,name1,age1,sex1,location1):
        self.name = name1
        self.age = age1
        self.sex = sex1
        self.location = location1
    def show(self):
        print("NAME: %s, AGE: %i, SEX: %s, LOCATION: %s "%(self.name , self.age, self.sex, self.location))
"""E1 = Employee()
E1.name = "Nikhil"
E1.age = 18
E1.sex = "Male"
E1.location = "Pune"
E1.show()"""

"""E2 = Employee()
E2.name = "Maya"
E2.age = 19
E2.sex = "Female"
E2.location = "Mumbai"
E2.show()"""
E1 = Employee("Nikhil", 18, "Male","Pune")
E2 = Employee("May", 19, "Female","Mumbai")
E3 = Employee("Ram", 21, "Male","Nashik")
E1.show()
E2.show()
E3.show()



 