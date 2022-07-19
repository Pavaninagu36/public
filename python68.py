#accept the number of days from the user and calculate the charge for library according to following.
#till live days   : Rs 2/day
#six to ten days  : Rs 3/day
#11 to 15 days    : Rs 4/day
#after 15 days    : Rs 5/day

a=int(input("enter number of days: "))
if a>1 and a<=5:
    c1=a*2
    print("charge from the library is:",c1)
elif a>=6 and a<=10:
    c2=a*3
    print("charge from the library is:",c2)
elif a>=11 and a<=15:
    c3=a*4
    print("charge from the library is:",c3)
elif a>15:
    c4=a*5
    print("charge from the library is:",c4)
else:
    print("no charge")
