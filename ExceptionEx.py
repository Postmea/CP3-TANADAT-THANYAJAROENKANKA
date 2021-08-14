import sys

randomList = ['a',5,8,10]

for i in randomList:
    try:
        print("The entry is ",i)
        r = 1/int(i)
        break
    except:
        print("Oops !!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",i,"is",r)