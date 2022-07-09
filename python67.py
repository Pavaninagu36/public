#wapp to calculate the eletricity bill(accept number of unit from user) ?

units=int(input("enter number of units: "))
cost1=(units-100)*5
cost2=(units-200)*10
units>200
if units<=100:
    print("no charge")
elif units>100 and units<=200:
    print("bill amount",cost1)
else:
    print("bill amount",cost2+500)
    
