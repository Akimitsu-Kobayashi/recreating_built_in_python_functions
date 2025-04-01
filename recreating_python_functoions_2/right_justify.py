#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

#inputs
text = input("Enter text: ")

space_with = input("space with: ")

space_count = int(input("Amount of right justify: "))

#make use of inputs to format result
if space_count > len(text):
    result = (space_with * (space_count - len(text))) + text 
else:
    result = text

#print result
print(result)