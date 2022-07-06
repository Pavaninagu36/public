#wapp the given number is divisible by 3,6,9. now impose multiple conditions

num=int(input("enter given  number is: "))

if num/3=='0' and num/6=='0' and num/9=='0':
    print("given number is divisible by 3,6,9")
else:
    print("given number is not divisible by 3,6,9")
