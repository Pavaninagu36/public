#wapp to find minimum number in given three values 10,98,66?

a=int(input("enter num1: "))
b=int(input("enter num2: "))
c=int(input("enter num3: "))
if a>b and a>c:
    print("maximim number is",a)
elif b>a and b>c:
    print("maximim number is",b)
else:
    print("maximim number is",c)
