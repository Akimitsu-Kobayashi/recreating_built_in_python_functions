#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

#ask user for text
text = input("Enter Text: ")

#ask what the text should be spaced with
spaces_with = input("space with: ")

#ask the count of the left adjust
spaces_count = int(input("How many: "))

result = text + (spaces_with*(spaces_count - len(text)))

#the | is an indicator for the amount of spaces there is
print(result + "|")



