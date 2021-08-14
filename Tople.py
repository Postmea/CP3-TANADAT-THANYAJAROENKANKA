#tuple จะคล้ายกับ list แต่มีข้อจำกัดคือไม่สามารถแก้ไข เพิ่ม ลบ ได้เลย
tuplelist = ("post","peem","dan")
print(tuplelist)

tuplelist2 = ("bank","fank")
print(tuplelist + tuplelist2)

tuplelist3 = tuplelist + tuplelist2
print(tuplelist3[0:3])
print(tuplelist2[1] in tuplelist3)

for i in tuplelist3:
    print(i)