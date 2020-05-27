def duplicate(s):
    t=[]
    for i in s:
        if i not in t:
            t.append(i)
    return t
s=list(map(int,input("enter the list : ").split(" ")))
print("list after removing duplicates : ",duplicate(s))

