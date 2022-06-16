
# Taking user-name
userName = str(input("Enter Your Name : "))

n = len(userName)

# Checking if it contains minimum 3 character
if n >= 3:
    print("Hello", userName, "How are you ?")
else:
    print("User Name contain at least 3 character")
