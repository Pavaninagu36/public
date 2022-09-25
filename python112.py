#wapp is a string a plindrome
string=input("enter any string:")
reverse_string=string[::-1]
print("the reversed string is:",reverse_string)
if string==reverse_string:
    print("the given string is palindrome")
else:
    print("it is not a palindrome")
