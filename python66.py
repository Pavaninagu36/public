#wapp ask user to enter total no.of seconds then your program has to print

seconds=int(input("enter total seconds: "))
hours=seconds /3600
remaining_seconds=seconds%3600
minits=remaining_seconds/60
remaining_seconds2=remaining_seconds%60
print(hours,minits,remaining_seconds2,sep=":")
