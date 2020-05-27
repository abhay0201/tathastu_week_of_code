def odd(n):
    if n%2!=0:
        return True
    else:
        return False
def prime(n):
    if n==1:
        return True
    for i in range(2,int(n**0.5)):
        if n%i==0:
            return True
    return False
def armstrong(n):
    s=len(str(n))
    m=n
    sum=0
    for i in range(s):
        sum+=(n%10)**s
        n=n//10
    if sum==m:
        return True
    else:
        return False
def palindrome(n):
    s=len(str(n))
    m=n
    sum=0
    for i in range(s):
        sum=sum*10+n%10
        n=n//10
    if sum==m:
        return True
    else:
        return False
n=int(input("enter a number : "))
if odd(n):
    print("it is an odd no")
else:
    print("it is an even no")
if prime(n):
    print("it is not a prime no")
else:
    print("it is a prime no")
if palindrome(n):
    print("it is a palindrome no")
else:
    print("it is not a palindrome no")
if armstrong(n):
    print("it is a armstrong no")
else:
    print("it is not a armstrong no")

      
        
        
