#5APR2022

#TRY AND EXCEPT IS USED TO SHOW A CUSTOM ERROR MSG WHEN ERROR OCCURS.

"""try:
    a = open("try_text1.txt")
    b = Hehe
except FileNotFoundError:
    print("The file is missing. We'll solve the issue soon.")
except Exception:
    print("Error in data type")"""
#The above is error handling for users i.e it is user friendly

#The below is error handling which is developer friendly

try:
    a = open("try_text1.txt")
    b = Hehe
except FileNotFoundError as c:
    print(c)
except Exception as d:
    print(d)