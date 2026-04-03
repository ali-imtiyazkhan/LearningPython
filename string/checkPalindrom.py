s = input("Enter a string : ")

for i in range(0,len(s)//2) :
    if s[i] != s[len(s)-i-1]:
        print("String is not a palindrome")
        break
else:
    print("String is a palindrome")