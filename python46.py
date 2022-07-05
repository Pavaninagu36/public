# wapp ask the user to enter any number verify the number is positive number or negitive number

num=float(input("Enter a number: "))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive number")
else:
    print("negative number")
