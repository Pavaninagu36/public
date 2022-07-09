#wapp that reads the length of the 3 sides of a triangle from the user.Then display a message that states the triangles type

x=int(input("enter first length: "))
y=int(input("enter second length: "))
z=int(input("enter thired length: "))

if x==y==z:
    print("equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("scalene triangle")
