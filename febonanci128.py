#wapp to print first 20 febonanci numbers

num=int(input("enter a number for terms: "))
n1=0
n2=1
count=0
if num<=0:
    print("enter positive number")
else:
    for i in range(0,num):
       print(count,sep=",")
       n1=n2
       n2=count
       count=n1+n2
