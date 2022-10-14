#23feb2022

#dir gives us all the attributes for the data type specified in the brackets

str1=dir(str) 
print("string attributes:   ", str1)
print("integer attributes:   ", dir(int))
print("float attributes:   ", dir(float))
print("list attributes:    ", dir(list))

#example of title attribute for sting which converts the first letter of string to upper case

var1= "nikhil sunil waghmode"
print(var1.title())