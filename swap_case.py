#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#input text
text = input("Enter text: ")
result = ""

#if the letter in text is upper case turn to lower case
for letters in text:
    if letters in uppercase_letters:
        for alphabet in range(len(uppercase_letters)):
            if uppercase_letters[alphabet] == letters:
                result += lowercase_letters[alphabet]
    else:
        for alphabet in range(len(lowercase_letters)):
            if lowercase_letters[alphabet] == letters:
                result += uppercase_letters[alphabet]

#print text
print(result)