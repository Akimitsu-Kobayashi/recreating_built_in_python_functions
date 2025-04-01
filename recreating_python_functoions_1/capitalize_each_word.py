#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

#ask user for text
text = input("Enter Text: ")

split_text = text.split()

for word in split_text:
    print(word.capitalize(),end=" ")

