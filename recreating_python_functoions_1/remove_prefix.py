#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#ask user for text
text = input("Enter Text: ")

#ask for the prefix to be removed
prefix = input("Enter prefix to be removed: ")

#create a defined function
def remove_prefix(text, prefix):
    #in any begining of the text if it is equal to the parameter to be removed it will be removed
    if text[0:len(prefix)] == prefix:
        return text[len(prefix):]
    else:
        return text

result = remove_prefix(text,prefix)

#print the resulting text
print(result)