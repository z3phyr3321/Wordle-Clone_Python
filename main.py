from random import randrange
import time

isCorrect = False
guess = None
word = ["apple", "balls", "cacti", "doing", "extra", "fiend", "guard", "house", "india", "jaded", "karen"]

randvalue = randrange(0, 10)
randomWord = word[randvalue]
print(randomWord)


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
            print(randomWord)
        elif isAgain == "n":
            isCorrect = True

    time.sleep(1)

    print()

print("---------------------------------------------------")
input(" Thanks for Playing ! ! !")
print("---------------------------------------------------")




    