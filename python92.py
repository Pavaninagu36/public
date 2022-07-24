# e power x calculation

x=int(input("enter the value of x: "))
n=int(input("enter the number of terms: "))
ex=0
for i in range(1,n):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
        ex=ex+(x**i)/(fact)
print(ex+1)     
