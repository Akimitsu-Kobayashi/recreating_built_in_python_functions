#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

#get input
is_lower = True

text = input("Enter text: ")

#check if lower
for letters in text:
    if "a" <= letters <= "z":
        is_lower = True
    else:
        is_lower = False
        break

#print result
print(is_lower)