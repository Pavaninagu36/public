#prime factor
num=int(input("enter an integer: "))
fac=2
while(fac<=num):
    if num%fac==0:
        print(fac,end=" ")
        num=num//fac
    else:
        fac=fac+1
