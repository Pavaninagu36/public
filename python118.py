#list of proper divisors
n=int(input("enter any number: "))
if n!=0:
    for i in range (1,n+1):
        div=n%i
        if div==0:
            print(i)
            i+=1
