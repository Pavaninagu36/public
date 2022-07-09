#wapp find the largest no from the given 3 numbers?

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if (num1>num2) and (num1>num3):
     print("largest number",num1)
elif (num2>num1) and (num2>num3):
     print("largest number",num2)
else:
     print("largest number",num3)
