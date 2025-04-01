#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

result = ""
left_spaces = 0

text = input("Enter text: ")

for letters in text:
    if letters == " " :
        left_spaces += 1
    else:
        break

print(text[left_spaces:])
print(left_spaces)
