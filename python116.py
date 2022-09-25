#avoiding duplicates
n=str(input("enter any string: "))
s=[]
s.append(n)
while n!=' ':
    n=str(input("enter next string: "))
    if n!=' ':
        if n not in s:
            s.append(n)
print(s)            
