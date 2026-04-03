s = input("Enter the string : ")
t= input("Enter the character to count : ")

# print("Frequency of ", t, " is: ", s.count(t))

counter = 0
for i in s:
    if i == t:
        counter += 1

print("Frequency of ", t, " is: ", counter)
