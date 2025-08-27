# 4. Write a program where the computer generates a random number between 1 
# and 10. The user has to guess the number. 
# If the guess is correct, print "Correct! You guessed it." and stop the 
# loop using break. 
# If the guess is wrong, ask again. 
import random
number=random.randint(1,10)
while True:
    guess=int(input("Enter the number:"))
    if guess==number:
        print("Correct! You guessed it")
        break
    else:
        print("Wrong, try again")