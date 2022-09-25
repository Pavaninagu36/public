#wapp to print lowercase and uppercase letters
char=input("enter any charecters:")
t=" "
for i in char:
    if i>="A" and i<="Z":
        t=t+i
print(t)        
