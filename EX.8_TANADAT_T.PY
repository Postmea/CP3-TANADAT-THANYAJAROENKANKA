UsernameInput = input("Username :")
PasswordInput = input("Password :")
if UsernameInput == "admin" and PasswordInput == "1234" :
    print("You are Authority")
    print("---- Welcome to My Iphone ----")
    print("select Product")
    print("1. Iphone 12 mini")
    print("2. Iphone 12")
    print("3. Iphone 12 pro")
    print("4. Iphone 12 pro max")
    A = "Iphone 12 mini"
    B = "Iphone 12"
    C = "Iphone 12 pro"
    D = "Iphone 12 pro max"
    priceA = 20000
    priceB = 27000
    priceC = 32000
    priceD = 41000
    userselected = int(input("Which one do you want ?? >>"))
    if userselected == 1:
        print("YOUR SELECTED IS",A,priceA,"THB")
        quantity = int(input("quantity >>"))
        vat = 7/100
        result = (priceA+(priceA*vat))*quantity
        print(result)
    elif userselected == 2:
        print("YOUR SELECTED IS",B,priceB,"THB")
        quantity = int(input("quantity >>"))
        vat = 7/100
        result = (priceB+(priceB*vat))*quantity
        print(result)
    elif userselected == 3:
        print("YOUR SELECTED IS",C,priceC,"THB")
        quantity = int(input("quantity >>"))
        vat = 7/100
        result = (priceC+(priceC*vat))*quantity
        print(result)
    elif userselected == 4:
        print("YOUR SELECTED IS",D,priceD,"THB")
        quantity = int(input("quantity >>"))
        vat = 7/100
        result = (priceD+(priceD*vat))*quantity
        print(result)
else:
    print("Wrong Username or Password")
print("Thank you, come back to visit again as soon.")