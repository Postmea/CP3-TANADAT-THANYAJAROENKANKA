def login():
    pass
    usernameInput = input("Usename : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showManu()
    else:
        return "Log in False"
def showManu():
    print("------- My Shop -------")
    print("1. Vat Calculator")
    print("2. Total Price")
    return manuSelect()
def manuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculate(totalPrice)
    if userSelected == 2:
        return priceCalculate()
    else :
        return "Error"
def priceCalculate():
    priceItem1 = int(input("Price Item 1 : "))
    priceItem2 = int(input("Price Item 2 : "))
    return vatCalculate(priceItem1 + priceItem2)
def vatCalculate(totalPrice):
    vat = 0.07
    calVat = totalPrice + (totalPrice * vat)
    return calVat

print(login())
