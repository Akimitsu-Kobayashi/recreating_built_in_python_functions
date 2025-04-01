#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

#get input
diff_case = ord("a") - ord("A")
result = ""

text = input("Enter text: ")

#compare ascii values
for letters in text:
    if "a" <= letters <= "z":
        result += chr(ord(letters) - diff_case)
    else:
        result += letters

#print result
print(result)