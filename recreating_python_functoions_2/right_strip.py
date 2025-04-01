#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

#get input
right_spaces = 0
is_first_space = True

text = input("Enter Text: ")

#remove spaces at the end
for letters in text:
    if is_first_space == True and letters == " ":
        pass
    elif is_first_space == True and letters != " ":
        is_first_space = False
    elif is_first_space == False and letters == " ":
        right_spaces += 1


#print the result
print(text[:len(text) - right_spaces] + "|")