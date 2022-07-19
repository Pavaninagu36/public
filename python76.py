#print the leap years in b/w your birth year to 2022

startyear=int(input("enter start year: "))
endyear=int(input("enter last year: "))
print("list of leap years: ")
for year in range(startyear , endyear):
    if(0==year%4) and (0!=year%100) or (0==year%400):
      print(year)  
