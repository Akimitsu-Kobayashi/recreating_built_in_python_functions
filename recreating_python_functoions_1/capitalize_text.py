#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

result = ""

#ask user for text
text = input("Enter Text: ")

for letters in range(len(text)):
    if letters == 0:
        result += text[letters].upper()
    else:
        result += text[letters].lower()

print(result)
