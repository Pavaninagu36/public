#wapp with one value appearing on each line. use eaither the sorted method or the sorted function to sorted the list.
n=int(input("enter any value: "))
s=[]
s.append(n)
while n!=0:
    n=int(input("enter next number: "))
    s.append(n)
print(s)    
s2=sorted(s)
print(s2)
