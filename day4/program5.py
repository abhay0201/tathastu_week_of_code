a=int(input("enter the no of candidates : "))
d=dict()
for i in range(a):
    c=(input("enter the name of candidate : "))
    e=int(input("enter the votes : "))
    d[c]=e
max_votes=0
candidate=""
for key,value in d.items():
    if value>=max_votes:
        if value==max_votes:
            if key<candidate:
                candidate=key
        else:
            max_votes=value
            candidate=key
print(max_votes,candidate)
