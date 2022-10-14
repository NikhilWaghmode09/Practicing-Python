#10march2022
#A list is declared using [], And it's mutable
#A tuple is declared using(), And it's immutable

list1=[1,2,3,4]
print(list1)
list1.append(5) #adds a value to the end of the list
print(list1)

tuple1=(1,2,3,4)
print(tuple1)
"""tuple1.append(5)
print(tuple1)"""  #this displays a error since tuple is immutable i.e you can't add anything to it later.

#tuples can be used to store credentials of users