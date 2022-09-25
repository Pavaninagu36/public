#The greatest common division of two positive numbers
m=int(input("enter first number: "))
n=int(input("enter second number: "))
if m>n:
    d=n
else:
    d=m
i=1
while d>i:
    if(m%i==0 and n%i==0):
        hef=i
        i=i+1
    print("the HCF is",hef)  
