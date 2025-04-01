#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

#inputs
text = input("Ener text: ")

suffix = input("Enter suffix to be removed: ")

#remove suffix
if text[len(text) - len(suffix):] == suffix:
    result = text[:len(text) - len(suffix)]
else:
    result = text

#print the result
print(result)