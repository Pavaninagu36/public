#wapp to find the sum of digits in any given number

num=int(input("enter a number: "))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("sum is: ",sum)    
    
