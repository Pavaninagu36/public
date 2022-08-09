#avoiding duplicates

n=str(input("enter any value: "))
s=[]
s.append(n)
while n>=' ':
    n=str(input("enter next number: "))
    if n!=' ':
        if n not in s:
            s.append(n)        
print(s)
