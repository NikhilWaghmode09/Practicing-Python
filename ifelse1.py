#30MAR2022

marks = {"Nikhil":90, "Tushar":110, "Soham":100, "Kedar": 120}
list1 = [45, 50, 45, 40]

def avg(v1):
    if type(v1) == dict:
        a = sum(marks.values())/len(marks)
        return a
    else:
        a = sum(list1)/len(list1)
        return a

print(avg(marks))
print(avg(list1))