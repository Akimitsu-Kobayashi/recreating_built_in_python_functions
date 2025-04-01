#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

text = input("Enter a text: ")
is_uppercase = False

for letter in text:
    if letter in lowercase_letters:
        is_uppercase = False
        break
    else:
        is_uppercase = True

print(is_uppercase)