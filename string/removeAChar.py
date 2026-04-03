s = input("Enter a string : ")
t = input("Enter a char to remove from the string : ")

newString = ""

for i in s :
    if i != t:
        newString += i

print("New string is: ", newString)