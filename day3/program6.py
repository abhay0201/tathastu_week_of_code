def sumlist(sublist):
    if len(sublist)==1:
        return sublist[0]
    sum=0
    for i in sublist:
        sum+=i    
    return sum
def powerset(l):
    k=(l.copy())
    for i in range(0,2**len(l)):
        k1=[]
        for j in range(len(l)):
            if i &(1<<j):
                k1.append(l[j])
        k.append(sumlist(k1))
    a=1
    while(True):
        if a not in list(set(k)):
            return a
        a+=1
l=list(map(int,input("enter the ist : ").split(" ")))
print(powerset(l))
