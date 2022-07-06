#wapp such that if the user enter above hundrade or blow 'zero' then the program has to generate an error massage stating that the input date is out of range.
#nested if condition

a=int(input("enter your marks: "))
if a<100 and a>0:
    if a>90:
        print("outstanding")
    elif a>80:
        print("excellent")
    elif a>60:
        print("very good")
    elif a>40:
        print("poor")
    else:
        print("fail")
 
