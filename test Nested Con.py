UsernameInput = input("Username :")
PasswordInput = input("Password :")
if UsernameInput == "admin" and PasswordInput == "1234" :
    print("You are Authority")
    print("---- My Shop ----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("What do you want ??")
    userselected = int(input(">>"))
    if userselected == 1:
        price = int(input("Price (THB) :"))
        vat = 7/100
        result = price+(price*vat)
        print(result)
    elif userselected == 2:
        price1 = int(input("First Product Price >>"))
        price2 = int(input("Second Product Price >>"))
        print(price1+price2)
else:
    print("Wrong Username or Password")