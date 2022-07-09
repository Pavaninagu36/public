#wapp the cost of the meal ordered at a resturent from the user.The out from your program should include the tax amount the tip amount and the grand total for the meal including both the tax and the tip

order=int(input("enter cost of the meal: "))
tax=order*0.18
tip=order*0.16
total=order+tax+tip
print("for the order amount of{} rupees,tax is{}, tip is{},total bill is{}".format(order,tax,tip,total))          
