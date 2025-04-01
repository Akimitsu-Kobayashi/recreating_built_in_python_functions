#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.


lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#input text
text = input("Enter text: ")
result = ""

#if the letter in text is upper case turn to lower case
for letters in text:
    if letters in uppercase_letters:
        for iteration in range(len(uppercase_letters)):
            if uppercase_letters[iteration] == letters:
                result += lowercase_letters[iteration]
    else:
        result += letters

#print text
print(result)