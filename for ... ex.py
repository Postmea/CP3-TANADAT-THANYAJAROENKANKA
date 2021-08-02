# วิธีที่ 1
userinput = int(input())
for x in range(userinput):
    text = ""
    for y in range(x+1):
        text += "*"
    print(text)


# วิธีที่ 2
userinput = int(input())
for x in range(userinput):
    print("*"*(x+1))


# สองวิธีมีให้ค่าเหมือนกัน
