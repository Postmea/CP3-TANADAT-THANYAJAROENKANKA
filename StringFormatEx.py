name = "Post"
weight = "66"
print("Hello "+name+", your weight is "+weight+" kg")  #ต่อข้อความแบบปกติ
print("Hello %s, your weight is %s kg" % (name,weight))  #ต่อข้อความแบบใช้ %s มาช่วย เพื่อให้อ่านง่าย
print("Hello %s, your weight is %f kg\n" % (name,99.99))
#ความหมาย %s = เหมาะกับ text
#ความหมาย %d = เหมาะกับ int จำนวนเต็ม
#ความหมาย %f = เหมาะกับ int ทศนิยม

name = input("Firstname : ").capitalize()  #คำสั่ง .capitalize() จะทำให้ตัวอักษรตัวแรกเป็นตัวพิมพ์ใหญ่
lastName = input("Lastname : ").capitalize()
print("\nHello %s %s, Your welcome\n" % (name,lastName))
welcome = "Welcome %s" % (name)
print(welcome.center(20,"-"))  #คำสั่ง .center จะทำให้ข้อความอยู่ตรงกลาง
print(len(name))  #คำสั่ง len จะเป็นการนับตัวอักษร
