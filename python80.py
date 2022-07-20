#units of pressure

kpa=float(input("enter pressure in kilopascals: "))
psi=kpa/6.895729
mmtr=kpa*770/101.325
atm=kpa/101.325
print("the pressure in pounds per square inch: ",psi)
print("the pressure in millmeters of memory: ",mmtr)
print("atmosphere pressure: ",atm)
