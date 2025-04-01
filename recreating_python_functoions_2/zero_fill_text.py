#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

#inputs
text = input("Enter text: ")

space_count = int(input("Amount of zero fill: "))

#make use of inputs to format result
if space_count > len(text):
    result = ("0" * (space_count - len(text))) + text 
else:
    result = text

#print result
print(result)