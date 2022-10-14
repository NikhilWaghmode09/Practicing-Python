#29MAR2022

list1 = [45, 50, 45, 40]

def avg1():
    print("THIS FUNCTIONS WORKS!") #this helps check if the function works or not
    a = sum(list1)/len(list1)
    return a

print(avg1()) #function is getting called here along with printing

marks = {"Nikhil":90, "Tushar":110, "Soham":100, "Kedar": 120}

def avg2(marks):
    b = sum(marks)/len(marks)
    return b

print(avg2(marks.values()))
