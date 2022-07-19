#wapp ask the user to enter no.of days as input and print the euielent years:months:days format?

number_of_days=int(input("enter number of days: "))
years=number_of_days//365
months=(number_of_days-years*365)//30
days=(number_of_days-years*365-months*30)
print(years,months,days,sep=":")
