n=int(input("enter a number : "))
a=0
b=n-1
while(a<=b):
    for i in range(n):
        if i==a or i==b:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    a+=1
    b-=1
    print()
while(a<n and b>=0):
    for i in range(n):
        if i==a or i==b:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    a+=1
    b-=1
    print()
