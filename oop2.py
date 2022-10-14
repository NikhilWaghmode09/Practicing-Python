class car:
    wheels = 4  #this is a class variable
    def __init__(self,brand):
        self.brand = brand  #this is object variable
        print("brand name:", self.brand)
        print("WHEELS:", car.wheels)
    def display(self):
        print("THIS IS THE VALUE",self.brand)

obj1 = car("TESLA")
obj2 = car("BMW")
obj1.display()