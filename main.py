from random import randrange
import time

isCorrect = False
isContinue = False
guess = None
word = ["apple", "balls", "cacti", "doing", "extra", "fiend", "guard", "house", "india", "jaded", "karen"]

randvalue = randrange(0, 10)
randomWord = word[randvalue]

print("---------------------------------------------------\n")
print(" Welcome to WORDLE(clone[on python])\n")

while isContinue == False:
    print("---------------------------------------------------")
    print("""Type 0 to START, 1 to DEBUG, 2 to QUIT or 3 to read the CREDITS) 
    """)
    print("---------------------------------------------------")
    chose = int(input(" > "))

    if chose == 0:
        isContinue = True
    
    elif chose == 1:
        print("---------------------------------------------------")
        print(" DEBUG MODE")
        print(" The word is", randomWord.upper())
        isContinue = True

    elif chose == 2:
        quit()

    elif chose == 3:
        print("---------------------------------------------------")
        print("       C R E D I T S\n")
        time.sleep(0.3)
        print(" W O R D L E (python edition)\n")
        time.sleep(0.3)
        print(" Original game made by Josh Wardle")
        time.sleep(0.3)
        print(" Owned by The New York Times")
        time.sleep(0.3)
        print(" Python version by yours truly")
        time.sleep(0.3)
        print("                       -Artemis")
        time.sleep(0.3)
        input(" Press ENTER > ")
    


while isCorrect == False:
    
    print("---------------------------------------------------")
    guess = input(" Your Guess\n > ").lower()
    lenght = len(guess)
    time.sleep(0.5)
    

    if len(guess) == len(randomWord):
        print("---------------------------------------------------")
        print(end=" ")
        for i in range(lenght):
            if guess[i] == randomWord[i]:
                print(guess[i].upper(), end=" ")
            else:
                print("-", end=" ")
        print()
            
    else:
        print("---------------------------------------------------")
        print(" Please insert only 5 letter words ! ! !")
    
    if guess == randomWord:
        time.sleep(1/2)
        print("---------------------------------------------------")
        print("\n You got it right ! ! !  Congratulations ! ! !\n\n")
        time.sleep(0.5)
        isAgain = input(" Do you wish to play again? (Y/N)\n > ").lower()

        if isAgain == "y":
            isCorrect = False
            randvalue = randrange(0, 10)
            randomWord = word[randvalue]
        elif isAgain == "n":
            isCorrect = True

    time.sleep(1)

    print()

print("---------------------------------------------------")
input(" Thanks for Playing ! ! !\n press ENTER to leave > ")
print("---------------------------------------------------")




    