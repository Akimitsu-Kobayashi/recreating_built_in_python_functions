#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

index_of_string = -1

#inputs
text = input("Enter text: ")

string_to_find = input("Enter text you want the index of: ") 

#find the first occurence of the string the user is finding the index of
for letter in reversed(range(len(text))):
    if text[letter:letter + len(string_to_find)] == string_to_find:
        index_of_string = letter
        break

#print its index
if index_of_string == -1:
    print("ValueError")
else:
    print(index_of_string)