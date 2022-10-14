#2APR2022

#FOR LOOP IS USED TO AVOID LONG CODES

#suppose we have to round figure the numbers from this list
A = [123.34, 3.14, 56.7]

for B in A:
    print(round(B))

#here B is the variable in which we store the edited values
for C in "hometown":
    print(C.upper())

#USING FOR LOOP FOR DICTIONARY

d1 = {"Nikhil":101.9, "Kevin":96.7, "Aditya":106.3}
for d2 in d1.items():
    print(d2)

#FOR DICTIONARY ITEMS MEANS VALUES AND KEYS COLLECTIVELY
for d2 in d1.keys():
    print(d2.upper())
    