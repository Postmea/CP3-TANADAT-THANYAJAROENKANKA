InputRound = int(input("Please input Round >>"))
sum = 0 #ตั้งค่าตัวแปลโดยให้การคำนวนเริ่มที่ 0
for x in range(InputRound):
    inputnumber = int(input("x"+str(x+1)+" :"))
    sum += inputnumber #ตัวเลขที่กรอกในแต่ละรอบมาบวกกัน
print(sum)