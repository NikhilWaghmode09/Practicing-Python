list1 = []
n = int(input("Enter number of students:"))
def stud():
    for i in range (0,n):
        print("Enter your marks:")
        m = int(input())
        list1.append(m)
    print(list1)
stud()

def cnt():
    global cnt1
    cnt1=0
    for i in list1:
        if i == -1:
            cnt1=cnt1+1
    print("Absent students:", cnt1)
cnt()  

def _avg():
    global sum1
    sum1=0
    for i in range(0,n):
        if list1[i]!=-1:
            sum1=sum1+list1[i]
        avg1=(sum1)/(n-cnt1)
    print("Average:",avg1)
_avg()

def low_high():
    test1=list1[0]
    for i in range(0,n):
        if list1[i]!=-1:
            if i<test1:
                test1=list1[i]
    print("Highest marks:", test1)
    
    test1=list1[0]
    for i in range(len(list1)):
        if list1[i]!=-1:
            if i>test1:
                test1=list1[i]
    print("Lowest marks:", test1)
low_high()

freq1={}
for i in list1:
    if i in freq1:
        freq1[i]+=1
    else:
        freq1[i]=1
print(freq1)
for i in freq1:
    j=1
    for j in freq1:
        if freq1[j]<freq1[i]:
            global c1
            c1=i
print("Marks with highest freqency:",c1)