# This is the Number Guessing game!
# You have 10 chances to guess what number I chose
# The range is 1-50 (inclusive)
# After the tenth guess, if you're wrong you lose!

#for random number generator on line 16
import random

#introduction
print("This is the Number Guessing Game")
print("I'm going to generate a random number between 1 and 50")
print("You will have 10 tries to guess the number")
print("After every guess I will be giving you a hint:")
print("[Higher] or [Lower]")
print("Now, lets begin!\n")

#generates outside of the loop
#if this was inside the loop, the user would be guessing a different nnumber each time
compC = random.randint(1,50)

#keeps track of the number of guesses
guessC = 1

#control variable for the loop
end = False
while end == False:
    print("I'll be keeping track of your guesses!")
    print("Guess #" + str(guessC))
    
    #checks if the user is over the guess limit of 10
    if guessC > 10:
        print("You ran out of guesses :(")
        print("You can always try again though! Good luck!!!")
        print("Here have a consolation cookie! (::)")
        break

    #control variable for user choice checker
    uCC = False
    while uCC == False:
        userG = input("Make your guess!: ") #gets input
        if not userG.isdigit():   #the isdigit ONLY checks if the characters used is 0-9
            print("Your guess must be a integer!")
            continue
            #we check if the input is a digit FIRST because if not we cant make a letter
            #into an integer, but we can make 7492 into an integer then check if its within the range
        userG = int(userG)  #must make input a integer before comparing it to integers 
        if userG >= 1 and userG <= 50:
            break
        else:
            print("Your guess must be between 1 and 50")
            continue
        

    #win condition
    if userG == compC:
        print("YOU GOT IT RIGHT GANGY WOAH!!!")
        print("It only took you " + str(guessC) + " amount of tries!")
        print("HAVE SOME COOKIES BRO BRO!")
        print("(::) (::) (::)")
        end = True
    #incorrect guess condition
    else: 
        #if guess is higher, hint is lower
        if userG > compC:
            print("Not quite there!")
            print("Your Hint as promised - [Lower]")
            guessC += 1
            continue
        #if guess is lower, hint is higher
        else:
            print("Not quite there!")
            print("Your Hint as promised - [Higher]")
            guessC +=1
            continue