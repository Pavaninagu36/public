#wapp leap year and not a leap year

y=int(input("enter a number: "))
if y%400==0:
    if y%100==0:
       print("It is not a leap year")
elif y%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
