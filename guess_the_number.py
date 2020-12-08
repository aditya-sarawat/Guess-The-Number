import time
import random


print("""
           Welcome To 'Guess The Number' Game
               Made By : Aditya Sarawat
               
               
        """)
initialAsk = input("Shall we play a game? Type YES or NO: ")

def quitGame():
    print("\n"
        "Goodbye, I hope to see you again!")
    time.sleep(3)
    quit()


while str.upper(initialAsk) != "YES":
    if str.upper(initialAsk) == "NO":
        quitGame()

    else:
        print("\n"
            "Sorry, I don't understand. \n")
        initialAsk = input("Shall we play a game? Type YES or NO: ")

else:
    play = True
    print("\n"
        "Let's get started! \n")


def gameStart():
    print("This game is called, 'Guess the number!' \n"
        "\n"
        "Here's how we'll play: \n"
        "I generate a random number, \n"
        "and you have to guess it. \n"
        "\n"
        "There are 3 difficulties: easy, medium or hard. \n"
        "The number ranges for each are as follows: \n"
        "EASY: 1 - 10 \n"
        "MEDIUM: 1 - 20 \n"
        "HARD: 1- 30 \n")

    guessRangeList = []

    modeSelectList = ["EASY", "MEDIUM", "HARD"]

    modeSelected = str.upper(input("Please enter your desired difficulty:  "))

    while modeSelected not in modeSelectList:
        print("\n"
        "Oops, that's not a valid difficulty. \n")
        modeSelected = str.upper(input("Please enter your desired difficulty:  "))

    else:
        if modeSelected == "EASY":
            for num in range(1, 11):
                guessRangeList.append(num)
            randomNumber = random.randint(1, 10)

        elif modeSelected == "MEDIUM":
            for num in range(1, 21):
                guessRangeList.append(num)
            randomNumber = random.randint(1, 20)

        elif modeSelected == "HARD":
            for num in range(1, 31):
                guessRangeList.append(num)
            randomNumber = random.randint(1, 30)

    print("\n"
    "%s mode selected. You have 3 tries to guess the correct number. \n" % (modeSelected))

    if modeSelected == "EASY":
        print("You have up to 3 hints.")
        hintsLeft = 3

    elif modeSelected == "MEDIUM":
        print("You have up to 12 hints.")
        hintsLeft = 12

    else:
        print("You have up to 21 hints.")
        hintsLeft = 21


    triesLeft = 3
    numbersAlreadyGuessed = []
    print("\n"
        "Tips: \n"
        "1. Type HINT and I will give you a number is not the correct number. \n"
        "2. Type LIST to see your previous guesses. \n")
    userGuess = input("Can you guess the number?  ")

    while userGuess != randomNumber:
        if str.upper(userGuess) == "LIST":
        
            if len(numbersAlreadyGuessed) > 0:
                numbersAlreadyGuessed.sort()
                print("\n"
                    "The numbers", numbersAlreadyGuessed, "have been guessed already. \n")
                userGuess = input("Can you guess the number?  ")
            
            else:
                print("\n"
                    "You have not currently guessed any number. \n")
                userGuess = input("Can you guess the number?  ")
    

        elif str.upper(userGuess) == "HINT":
        
            if hintsLeft > 0:
                numberOptions = [num for num in guessRangeList if num != randomNumber and num not in numbersAlreadyGuessed]
                hintedNumber = (random.choice(numberOptions))
                numbersAlreadyGuessed.append(hintedNumber)

                print("\n"
                    "You used a hint. %d is NOT the number you're looking for. \n" % (hintedNumber))

                hintsLeft -= 1

                if hintsLeft > 1 or hintsLeft == 0:
                    print("You have %d hints left." % (hintsLeft))

                else:
                    print("You have %d hint left." % (hintsLeft))

                print()
                userGuess = input("Can you guess the number?  ")
            
            else:
                print("\n"
                    "Sorry, you have no more hints. \n")
                userGuess = input("Can you guess the number?  ")
    

        elif userGuess.isdigit() == True:

            if int(userGuess) != randomNumber:      
                print()

                if int(userGuess) in guessRangeList:     
            
                    if int(userGuess) not in numbersAlreadyGuessed:     
                        print("Oops, that's not the number I'm looking for. \n")
                        numbersAlreadyGuessed.append(int(userGuess))
                        triesLeft -= 1

                        if triesLeft >= 1:    

                            if triesLeft > 1:     
                                print("You have %d tries left." % (triesLeft))

                            elif triesLeft == 1:     
                                print("You have %d try left." % (triesLeft))

                            print()
                            userGuess = input("Can you guess the number?  ")

                        else:     
                            print("Sorry, you have run out of tries. The correct number was %d. \n" % (randomNumber))
                            askPlayAgain = input("Type 'EXIT' to exit, or 'PLAY' to play again: ")

                            while str.upper(askPlayAgain) != "PLAY":    

                                if str.upper(askPlayAgain) == "EXIT":  
                                    quitGame()

                                else:   
                                    print("\n"
                                        "Sorry, I don't understand. \n")
                                    askPlayAgain = input("Type 'EXIT' to exit, or 'PLAY' to play again: ")

                            else:    
                                print()
                                gameStart()

                    else:       
                        print("Oops, you've already guessed that number. \n")
                        userGuess = input("Can you guess the number?  ")

                else:      
                    print("Oops, that's not in the range. \n")
                    userGuess = input("Can you guess the number?  ")

            else:     
                print("\n"
                    "Congratulations! You guessed correctly!")
                time.sleep(3)
                quit()

        else:
            print("\n"
                "Sorry, I don't understand. \n")
            userGuess = input("Can you guess the number?  ")

gameStart()
