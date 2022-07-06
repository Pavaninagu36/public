#in this excercise you will create a program that reads a letter of the alphabet from the user. if the user enters a,e,i,o,u then your program should display a message indicating that the entered letter is vowel.if the user enters y then your program should display a message indicating that some times y is a vowel, and sometimes y is a constant otherwise your program should display a message indicating that the letter is constant

char=str(input("enter any alphabet: "))

if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print("The alphabet entered by the user is a vowel")
else:
    print("The alphabet entered by the user is not a vowel")
