#wapp that asks the user to enter date range and print output as zodiac sign.
a_12="dec"
a_1="jan"
a_2="feb"
a_3="march"
a_4="april"
a_5="may"
a_6="june"
a_7="july"
a_8="aug"
a_9="sep"
a_10="oct"
a_11="nov"
m=str(input("enter the string for month: "))
d=int(input("enter the date: "))
if (m==a_12 and d>=22) or (m==a_1 and d<=19):
    print("capricom")
elif (m==a_1 and d>=20) or (m==a_2 and d<=18):
    print("aquarius")
elif (m==a_2 and d>=19) or (m==a_3 and d<=20):
    print("pisces")
elif (m==a_3 and d>=21) or (m==a_4 and d<=19):
    print("aries")
elif (m==a_4 and d>=20) or (m==a_5 and d<=20):
    print("tauras")
elif (m==a_5 and d>=21) or (m==a_6 and d<=20):
    print("gemini")
elif (m==a_6 and d>=21) or (m==a_7 and d<=22):
    print("cancer")
elif (m==a_7 and d>=23) or (m==a_8 and d<=22):
    print("leo")
elif (m==a_8 and d>=23) or (m==a_9 and d<=22):
    print("virgo")
elif (m==a_9 and d>=23) or (m==a_10 and d<=22):
    print("libra")
elif (m==a_10 and d>=23) or (m==a_11 and d<=22):
    print("scorpio")
else:
    print("sagittarius")
    
    
    
    
    
    
    
    
