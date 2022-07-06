#the length of a month varies from 28 to 31 days. In this excersics you will create a program that reads the name of a month from the user as a string.Then your program should display the no of days in that month.Display "28 or 29" days for february so that leap year are addressed.

month=str(input("enter name of the month: "))
if month=='january' or month=='march' or month=='may' or month=='july' or month=='august' or month=='october' or month=='december':
    print("The month consists 31 days")
elif month=='april' or month=='june' or month=='september' or month=='november':
    print("the month consists 30 days")
elif month=='febuary':
    print("The month consists of 29 days")
else:
    print("The month not consists of abvoe 31 days")
