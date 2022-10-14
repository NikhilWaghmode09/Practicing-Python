import module1
#End sem ki practice chal rahi dosto!

"""
str1 = "HELLO"
ad1 = id(str1)
print(ad1)
str1 = "Helmo"
ad2 = id(str1)
print(ad2)
if ad1==ad2:
    print("AYO HOW TF POSSIBLE.")
else:
    print("Yo everything's clear")
def str(self):
    print(id(self))

str(str1)"""

"""def fun1(a1,a2):
    "This is a doc sting
    haha actually this funtion adds two numbers."
    a3=a1+a2
    return a3
print(fun1(3,4))
print(fun1.__doc__)"""


#1 PROGRAM TO CALCULATE AREA OF CIRCLE(using functions)

def area_circle(r):
    area = 3.14 *r*r
    return area
    
print("Area of circle:",area_circle(10))

#2 PROGRAM TO CALCULATE SUM(using functions)

def sq(num1):
    sq = num1*num1
    print("The square is %d."%sq)
"""sq(13)"""

#3 PROGRAM TO SWAP TWO NUMBERS(using functions)

def swap(a,b):
    print("Numbers before swaping are %i & %d."%(a,b))
    c = a
    a = b
    b = c
    print("Numbers after swaping are %i & %d."%(a,b))
"""swap(4,9)"""

#4 program using function to find greatest of three numbers by passing numbers as arguments.
def grt(a,b,c):
    if a>b and a>c:
        print("a is the greatest number.")
    elif b>a and b>c:
        print("b is the greatest number.")
    else:
        print("c is the greatest number.")
"""x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
z = int(input("Enter your third number: "))"""

"""grt(x,y,z)"""

#5 A python program to demonstrate difference between local and global variable.

a = 10 
#print("this is global variable:",a)
def f1():
    a = 20 
    print("this is local variable:",a)
"""f1()"""

def fun():
    x=6
    return
"""print(fun())"""

#required argument
def arg(name,age):
    print(name)
    print(age)

"""arg("shyam", 18)
arg("ram", 19)"""

#default argument
def arg1(name,age="18"):
    print(name)
    print(age)

"""arg1("shyam")
arg1("ram", 19)"""

#keyword argument
def arg2(name,age):
    print(name)
    print(age)

"""arg2(age=18, name="shyam")
arg2(name="Ram", age=19)"""

#variable length argument
def arg3(a,*tup1):
    sum1 = a
    for i in tup1:
        sum1= sum1 + i
    print(sum1)
"""arg3(10,8,4)"""

#lambda funtion
sum2=lambda x,y :x+y
"""print(sum2(12,2))"""


module1.add1(2,3)

#strings

#string operations

#crasr
a = "GOOD"
b =  "MORNING"
print(a+b)
a+=b
print(a)
print(a*2)
print(a[2])
print(a[:-2

])