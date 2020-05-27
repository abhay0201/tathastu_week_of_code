def duplicate(s):
    t=""
    for i in s:
        if i not in t:
            t+=i
    return t
s=input("enter string : ")
print("string after removing duplicates : ",duplicate(s))

