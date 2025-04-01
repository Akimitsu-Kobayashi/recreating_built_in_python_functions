#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

count = 0

#inputs
text = input("Enter text: ")

letter_to_count = input("Enter text to count: ") 

#count letter 
for letters in text:
    if letters == letter_to_count:
        count += 1

#print count
print(count)