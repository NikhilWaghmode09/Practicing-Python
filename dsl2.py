"""fb =[]
n = int(input("Enter number of football players."))
for i in range (0,n):
    a=input("Enter students who play Football.")
    fb.append(a)
cr =[]
n = int(input("Enter number of football players."))
for i in range (0,n):
    a=input("Enter students who play Football.")
    cr.append(a)
bad =[]
n = int(input("Enter number of football players."))
for i in range (0,n):
    a=input("Enter students who play Football.")
    bad.append(a) 
"""
def interstn(lst1,lst2):
    lst3 = []
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return lst3;
    #print(lst3)
fb = [1,5,3,4]
cr = [2,3,4,6]
bd = [3,4,5,10]
FnC = interstn(fb,cr)
#print(FnC)
FnB = interstn(fb,bd)
#print(FnB)
CnB = interstn(cr,bd)
print("List of Students who play both Cricket and Badminton:",CnB)
def union(lst1,lst2):
    lst4 = lst2.copy()
    for i in lst1:
        if i not in lst4:
            lst4.append(i)
    return lst4;
CuB = union(cr,bd)
def diff(li1,li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif;
print("Number of students who play either cricket or badminton but not both :",diff(CuB,CnB))