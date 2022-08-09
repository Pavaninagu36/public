#reverse order

n=int(input("enter any value: "))
s=[]
s.append(n)
while n!=0:
    n=int(input("enter next number: "))
    s.append(n)
s.reverse()        
print(s)
