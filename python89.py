#square root
#write a program that implements newton's method to compute and display the square root of a number ,x,entered by the user.the algorithem for newton's method follows
x=int(input("enter any number: "))
guess=x/2
while ((guess**2)-(x))>=10e-12:
    guess=(guess+(x/guess))/2
print('the square root of',x,'is',guess)           
    
