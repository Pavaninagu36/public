#convert an integer to its ordinal number

def num(a):
    if a<=12:
        if a==1:
            print("first")
        elif a==2:
            print("second")
        elif a==3:
            print("third")
        elif a==4:
            print("fourth")
        elif a==5:
            print("fifth")
        elif a==6:
            print("sixth")
        elif a==7:
            print("seventh")
        elif a==8:
            print("eigtht")
        elif a==9:
            print("ninth")
        elif a==10:
            print("tenth")
        elif a==11:
            print("eleventh")
        elif a==12:
            print("twelveth")
a=int(input("enter any number: "))
num(a)
