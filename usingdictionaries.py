#25feb2022
#Dictionaries are different than list because it saves label along with value
#SYNTAX var1={KEY:VALUE}

marks = {"Nikhil":90, "Tushar":110, "Soham":100, "Kedar": 120}

print(type(marks))
print(marks.values())
print(marks.keys())

sum1=sum(marks.values())
len1=len(marks)
avg1=sum1/len1
print("The average percentage is:",avg1)


#29MAR2022
print("THESE ARE SOHAM'S MARKS:", marks["Soham"])
print( list(marks.keys())[list(marks.values()).index(110)])
"""first we convert marks.keys to list then we use slicing to get the index we desire to find key of
then we convert marks.value to list and use list's property of index to find the value at the index."""