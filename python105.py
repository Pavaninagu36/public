#wapp with one value appearing on each line. use eaither the sort method or the sorted function to sort the list.
n=int(input("enter any value: "))
s=[]
while n!=0:
    n=int(input("enter next number: "))
    s.append(n)
s.sort()
print(s)
