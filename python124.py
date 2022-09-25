#wapp to print alphabets

n=7
num=65
for i in range(0,n):
    for i in range(0,i+1):
        ch=chr(num)
        print(ch,end=" ")
        num=num+1
    print(" ")    
