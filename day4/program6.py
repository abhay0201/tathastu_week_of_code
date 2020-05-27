a=int(input("enter the no of words in dictionary : "))
dict=[]
for i in range(a):
    dict.append(input("enter the word :"))
b=int(input("enter the no of words in dictionary : "))
list=[]
for i in range(b):
    list.append(input("enter the letter :"))
l=[]
for i in dict:
    if set(i).issubset(set(list)):
        l.append(i)
print(",".join(l)+".")
