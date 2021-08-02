CorrectNumber = 68
UserGuess = 0
while UserGuess != CorrectNumber:
    UserGuess = int(input("Please guess your number >>"))
    if UserGuess > CorrectNumber:
        print("Too Large")
    elif UserGuess < CorrectNumber:
        print("Too Small")
    elif UserGuess == CorrectNumber:
        print("You are correct number.")
