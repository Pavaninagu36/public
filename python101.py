#mobile bill

minu=int(input("enter min: "))
msg=int(input("enetr msg: "))
if minu>50 and msg<50:
    x=(minu-50)*0.25+(msg-50)*0.15+0.44+15.00
    y=x*0.05
    z=y+x
    print(z)
elif minu>50 and msg<=50:
    x=(minu-50)*0.25+0.44+15.00
    y=x*0.05
    z=y+x
    print(z)
elif minu<=50 and msg>50:
    x=(msg-50)*0.15+0.44+15.00
    y=x*0.05
    x=y+x
    print(z)
else:
    x=15.00+0.44
    y=x*0.05
    z=y+x
    print(z)
    
