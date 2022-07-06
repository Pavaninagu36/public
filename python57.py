#wapp that determines the name of a shape from its no of sides.Read the no of sides from the user and then report the approriate name is part of a meaningfull meassage your program should support shaps with anywhere from 3 upto(and including) 6sides.if a number of sides outsides this range is entered then your program should display an apprpriate error message.

a=int(input("enter any number: "))
if a<3 or a>6:
    print("out of range")
elif a==3:
    print("it is a triangle")
elif a==4:
    print("it is a reactangle")
elif a==5:
    print("it is a pentagonal")
elif a==6:
    print("it is a hexagonal")
else:
    print("out of range")
