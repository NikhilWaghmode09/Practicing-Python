"""import module1
a= int(input("Enter your first number:"))
b= int(input("Enter your second number:"))
module1.add(a,b)"""


def ord1(x):
    print("The ASCII code for the character is:", ord(x))
#y=input("Enter your character:")
#ord1(y)

try1= 'Hello World'

"""print(try1.isdigit())
print(try1.isalnum())
print(try1.capitalize())
print(try1.isalpha())
print(try1.islower())
print(try1.isupper())"""
#iterating through a string using for loop
"""for i in try1:
    print(i, end='')
print('''

''')"""
#iterating through a string using while loop
"""index=0
while index < len(try1):
    print(try1[index],end='')
    index+=1"""

def display(name, age=18):
    print("Name:%s Age:%d" %(name,age))
'''display("Nikhil",19,22)
display("Himesh")'''

def try2(*x):
    print(x)
#try2("Nikhil", 18,100)
a=1
b=2
l1 =lambda a,b:a+b
print(l1(a,b))
print(id(a))
a+=1
print(id(a))