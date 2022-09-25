#check a password

def np(n):
    p=n+1
    for i in range(2,p):
        if p%i==0:
            p=p+1
        else:
            print(p,end=" ")
