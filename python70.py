v=float(input("enter wind speed in kilometers/hours: "))
t=float(input("enter air temperature in degrees celsius: "))
wci=13.12+0.6215*t-11.37*v**(0.16)+0.3965*t*v**(0.16)
print("the wind chill index is",wci)
