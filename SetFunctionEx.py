userInput = int(input("Enter number that you want : "))
myFruits = set()
while(len(myFruits)<userInput):
    myFruits.add(input("Fruits : ").lower())
    print(myFruits)