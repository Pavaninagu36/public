# fizz-buzz

for i in range(1,101,1):
    if(i%3)==0 and (i%5==0):
        print("player says both fizz and buzz instead of their number: ")
    elif(i%3==0):
       print("player says  fizz  instead of their number: ")
    elif(i%5==0):
        print("player says  buzz instead of their number: ",i)
    else:
        print("player says number is not divisible by 3 and 5: ",i)
        
