#write a python program to swap 2 numbers

x=5
y=10

x=input("enter value of x: ")
y=input("enter value of y: ")

#create a temporary variable and swap the values
temp=x
x=y
y=temp

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))
