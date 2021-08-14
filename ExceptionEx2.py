try:
    text1 = int(input("A : "))
    text2 = int(input("B : "))
    print(int(text1/text2))
except ValueError:
    print("Please entry by number")
except ZeroDivisionError:
    print("Can't division by zero !!")