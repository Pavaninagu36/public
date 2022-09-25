#wapp to add multiple numbers which are combination of +ve and -ve numbers
n=int(input("enetr length: "))
totlst=[]
i=0
while(i<n):
    totlst.append(int(input("enter another num: ")))
    i=i+1
print(totlst)
plst=[]
nlst=[]
for i in totlst:
    if (i>0):
        plst.append(i)
    else:
        nlst.append(i)
print(plst)
print(nlst)
