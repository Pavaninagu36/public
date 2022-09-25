#wapp to count the no.of times a charater occurs in the given string(a to z)checking
string="python programming"
list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(list)):
    count=0
    for j in list:
        if string[i]==j:
            count=count+1
        else:
            pass
        print(count)
