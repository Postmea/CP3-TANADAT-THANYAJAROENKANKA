username = input("username : ")
password = input("password : ")
timeLeft = 3
LoginExceed = 3
while username != "Admin" or password != "1234":
    timeLeft -= 1
    LoginExceed = 3
    print("- Invalid username or password -")
    if timeLeft == 0:
        print("- Login exceed (3) -")
        print("--------------------")
        break
    username = input("username : ")
    password = input("password : ")
else:
    print("- Successful login -")