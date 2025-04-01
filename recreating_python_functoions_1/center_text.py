#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

#ask user for text
text = input("Enter Text: ")

#ask what the text should be spaced with
spaces_with = input("space with: ")

#ask the count yo br centered
space_count = int(input("How many: "))

#calculate spaces
all_spaces = space_count - len(text)

#left and right spacing
left_spacing = all_spaces // 2
right_spacing = all_spaces - left_spacing

#formats the spacing 
result = (spaces_with*left_spacing) + text + (spaces_with*right_spacing)

#prints the centered text
print(result)