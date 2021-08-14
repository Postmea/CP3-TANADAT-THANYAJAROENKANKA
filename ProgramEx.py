menu = {"ข้าวหมกไก่":45,"ข้าวหน้าปลาแซลม่อน":150,"ข้าวหมูกรอบไข่มะตูม":65,}
menuList = []

def showBill():
    print("------- My Food Station -------")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])

while True:
    menuName = input("Please Enter Manu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,menu[menuName]])

print(menuList)
showBill()
