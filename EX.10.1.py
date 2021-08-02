start = int(input("start :"))
step = int(input("step :"))
result = 0
for i in range(5):
    result += start + step * i + 1
    print(result)

# วิธีคิด
# += คือการเอาค่าที่คำนวนได้มาบวกกันในแต่ละรอบ
# 1 + 2 * 0 + 1 = 2
# 1 + 2 * 1 + 1 = 4
# 1 + 2 * 2 + 1 = 6
# 1 + 2 * 3 + 1 = 8
# 1 + 2 * 4 + 1 = 10
