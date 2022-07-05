#wapp to convert number from other system into decimal number system. use format operator

num=input("enter a binary number: ")

decimal_num1=int(num,2)
decimal_num2=int(num,16)
decimal_num3=int(num,8)

print("The binary to decimal {} is {}".format(num,decimal_num1))
print("The octal to decimal {} is {}".format(num,decimal_num2))
print("The decimal equivelent {} is {}".format(num,decimal_num3))
