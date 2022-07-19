#if the user enter 3141 then your program should display 3+1+4+1=9?

a=int(input("enter a four digit number: "))
x=a/100
x1=(a-x*1000)//100
x2=(a-x*1000-x1*100)//10
x3=(a-x*1000-x1*100-x2*10)
print("The sum of four digits number is ",x+x1+x2+x3)
