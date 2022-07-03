#write a python pyprogram enter the marks uptained all 5 subjects based on the input data calculate average,percentage,used in split and separate functions?

sub1,sub2,sub3,sub4,sub5=input("enter english,math,computer,physics,chemistry marks: ").split()

Total=sub1+sub2+sub3+sub4+sub5
Average=Total/5
Percentage=(Total/500)*100

print(sub1,sub2,sub3,sub4,sub5,sep=" ")
print("the total= ",Total)
print("the average= ",Average)
print("the percentage= ",Percentage)

      
