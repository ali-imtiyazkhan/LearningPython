s = input("Enter your emailId: ")

# username = s.split("@")[0]

# print("Username is: ", username)

pos = s.index("@")

username = s[0:pos]

print("Username is: ", username)