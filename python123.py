#random lottery number
s=[]
for i in range(6):
    num=int(input("enter any number: "))
    if num!=0:
        if num not in s:
            s.append(num)
        else:
            num=int(input("enter number: "))
            s.append(num)
s.sort()
print(s)
