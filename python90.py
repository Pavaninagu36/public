#range function
#wapp to print the number which are divisible by 4 but not divisible by 8. consider the number between 1 to 100.

for i in range(1,101):
    if i%4==0 and i%8!=0:
       print(i)
