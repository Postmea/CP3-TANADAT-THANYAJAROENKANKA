word = {"Bird":"นก","Worm":"หนอน","Dog":"หมา"}
print(word)

print(word.keys())   #.keys() คือการดึงหัวตาราง
print(type(word.keys()))

print(word.values())   #.values() คือการดึงค่าของตาราง
print(type(word.values()))

for i in word.values():
    print(i)