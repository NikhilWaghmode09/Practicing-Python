#28MAR2022
"""METHODS OF LIST"""

list1=[1,2,3,4,5,6,7,8]
#APPEND AND CLEAR
#append adds a value at the end of the list
list1.append(9)
list1.append("TEN")
"""list1.clear() #clears the list"""

print("THIS IS THE LIST:", list1)

#INDEX 
#Index is used to find postion of the object in the list
print("THIS IS INDEX:")
vara = list1.index(3)
print(vara)

#GET VALUE USING INDEX
list2=[78,65,34,54,21,30,24,69,90,25,12]
varb = list2.__getitem__(3) #you could also use only [] instead of __getitem__()
varc = list2[3]
print("THIS IS ITEM FROM INDEX:", varb)
print("THIS IS ITEM FROM INDEX ANOTHER METHOD:", varc)


#REVERSE
print("THIS IS REVERSED LIST:")
list1.reverse()
print(list1)

#LIST SLICING
#used for extracting a set of elements from list 

print("THIS IS SLICED LIST2:",list2[2:8])

#NEGATIVE INDEXING 
#starts from end of the list
list3=[45,165,164,15,45,15,68,14,32,78,56]
print("THIS IS LENGTH OF LIST3:", len(list3))
print("THIS IS NEGATIVE SLICING:", list3[-4:-1])