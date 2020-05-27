a=int(input("enter the no of keys in dictionary : "))
d=dict()
for i in range(a):
    c=int(input("enter the key : "))
    e=int(input("enter the value : "))
    d[c]=e
print("second maximum element : ",list(sorted(d.values()))[-2])
