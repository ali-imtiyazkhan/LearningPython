s = input("Enter a string : ")
L = []
newstring = ''

for i in s.split():
    newstring += i[0].upper() + i[1:].lower()
    L.append(newstring)

print(" ".join(L))    
