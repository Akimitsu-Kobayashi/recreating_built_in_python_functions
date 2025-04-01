#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

#ask user for text
text = input("Enter Text: ")

#ask for what to check the texts ends with to be removed
endswith = input("does the text ends with: ")

#check if the last letters match with endswith
if text[len(text)-len(endswith):] == endswith:
    print("True")
else:
    print("False")
