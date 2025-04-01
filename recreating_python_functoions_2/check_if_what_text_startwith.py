#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

#inputs
does_startwith = True

text = input("Enter text: ")

startwith = input("does the text start with: ")

#check if string starts with string
if text[:len(startwith)] == startwith:
    does_startwith = True
else:
    does_startwith = False

#print the bool
print(does_startwith)
