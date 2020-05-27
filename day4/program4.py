a=int(input("enter the no of keys in dictionary : "))
d=dict()
for i in range(a):
    c=int(input("enter the key : "))
    e=int(input("enter the value : "))
    d[c]=e
d1=dict()
l=list(d.keys())
for key in l:
    if d[key] not in d1.values():
        d1[key]=d[key]
print(d1)
