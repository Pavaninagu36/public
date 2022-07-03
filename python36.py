#write the python program to enter the marks 5 subjects based on the input data calculate average and percentage

english=float(input("Enter English marks: "))
math=float(input("Enter Math marks: "))
computer=float(input("Enter Computer marks: "))
physics=float(input("Enter Physics marks: "))
chemistry=float(input("Enter Chemistry marks: "))

Total=english+math+computer+physics+chemistry
Average=Total/5
Percentage=(Total/500)*100

print("\nTotal Marks = %.2f" %Total)
print("Average Marks = %.2f" %Average)
print("Marks Percentage = %.2f" %Percentage)



