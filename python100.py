#wapp that reads a magnitude from the users&display the appropriate descriptor as part of a meaningfil message for ex: it the user enters 5.5 then
a=int(input("enter magnitude: "))
if a<2:
    print("micro")
elif a>=2 and a<3:
    print("very minor")
elif a>=3 and a<=4:
    print("minor")
elif a>=4 and a<5:
    print("light")
elif a>=5 and a<6:
    print("moderate")
elif a>=6 and a<7:
    print("strong")
elif a>=7 and a<8:
    print("major")
elif a>=8 and a<10:
    print("great")
else:
    print("meteoric")
