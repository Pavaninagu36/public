#ask the user to enter any string,which is the combination of upper case&lower case,now your program has to be print upper case letters?
char=input("enter any charecters: ")
t=" "
for i in char:
    if i>="A" and i<="Z":
        t=t+i
print(t)        
