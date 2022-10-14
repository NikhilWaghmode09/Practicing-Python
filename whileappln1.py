#4APR2022

#This is password checker using while loop
#we take examples in input until it matches the desired password the code keeps executing

"""mypassword = ""
while mypassword != "1234":
    mypassword = input("Enter a 4 digit password: ")"""

#other way of doing using breaks. this one's more friendly

pass1 = ""
while True:
    pass1 = input("enter a five digit password: ")
    if pass1 == "12345":
        break
    else:
        continue