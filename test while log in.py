UsernameInput1 = input("Username >>")
UsernameInput2 = input("Password >>")
while UsernameInput1 != "admin" or UsernameInput2 != "1234":
    print("You are not authority")
    UsernameInput1 = input("Username >>")
    UsernameInput2 = input("Password >>")
print("You are authority")