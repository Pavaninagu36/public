#sort 3 integers

x=int(input("enter first number: "))
y=int(input("enter second number: "))
z=int(input("enter thied number: "))
a1=min(x,y,z)
a2=max(x,y,z)
a3=(x+y+z)-a1-a2
print("numbers in sorted order: ",a1,a2,a3)
