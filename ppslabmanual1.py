"""BP=int(input("Basic Pay:"))
HRA=BP*(10/100)
TA=BP*(5/100)
Tot_Sal=BP+HRA+TA
PT=Tot_Sal*(2/100)
Pay_Sal=Tot_Sal-PT
print("Salary payable after deductions=", Pay_Sal)
"""

"""print("Calculator")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.num1 to the power num2")
print("6.Factorial of a number(num!)")
choice=input("Enter choice(1/2/3/4/5/6):")
if choice ==("1"or"2"or"3"or"4"or"5"):
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
else:
    num=int(input("Enter number:"))
if choice=="1":
    print("Addition=", num1+num2)
elif choice=="2":
    print("Substraction=", num1-num2)
elif choice=="3":
    print("Multiplication=", num1*num2)
elif choice=="4":
    print("Divison=", num1/num2)
elif choice=="5":
    print("num1 to the power num2=", num1**num2)
elif choice=="6":
    fac=1
    i=1
    while i<=num:
        fac=fac*i
        i=i+1
    print("Factorial of",num,"is",fac)
else:
    print("Invalid input") 
"""


"""list1=[]
avg=0
total=0
print("Enter how many number u want to enter in list")
n=int(input())
print("Enter number to insert in list")
for i in range(0,n):
    x=int(input())
    list1.append(x)
print("List Element are: ",list1)
print("Maximum number is:",max(list1)) 
print("Minimum number is:",min(list1))
for i in range(0,n):
    total+=list1[i]
    avg=total/n
print("Sum of list Element:",total)
print("Average of list element is:",avg)"""


"""import math
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial=",fact) 
n=int(input("Enter a number"))
print("Square root=",math.sqrt(n))
print("Square=",math.pow(n,2)) 
print("Cube=",math.pow(n,3))
factorial(n)"""



"""s=input("Enter a string: ")
print("1.Length\n2.Reverse \n3.Equality of two strings \n4.Check Palindrome \n5.Check substring")
choice = int(input("Enter your choice: "))
if choice == 1:
    print('Length of string is ',len(s))
elif choice == 2:
    print('Reverse string is ',s[::-1])
elif choice == 3:
    s2= input("Enter string to compare: ")
    if s== s2:
        print("Equal")
    else:
        print("Not equal")
elif choice == 4:
    if s== s[::-1]:
        print("Palindrome")
    else:
        print("Not palindome")
elif choice == 5:
    s2= input("Enter substring to check: ")
    if s2 in s:
        print("Substring present")
    else:
        print("Substring absent")
else:
    print("Invalid Choice")"""

"""f1= open("file1.txt", "r")
print(f1.name)
print(f1.closed)
print(f1.mode)
f1.close()
print(f1.closed)
f1= open("file1.txt", "w")
f1.write("bye")
f1= open("file1.txt", "r")
print(f1.read())
f1.close()
"""

class Comp:
    def config(self):
        print("i5, 12gb")

