l1=list(map(int,input("enter the first list : ").split(" ")))
l2=list(map(int,input("enter the second list : ").split(" ")))
l=[]
for i in l1:
    if i in l2:
        l.append(i)
print("list after intersection of l1 and l2 :",l)
