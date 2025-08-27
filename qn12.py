# 8. Write a program that keeps taking numbers as input from the user. 
# If the number is not zero, print "You entered: <number>". 
# If the number is 0, stop the loop. 
# Input: 4 → You entered: 4 
# Input: 9 → You entered: 9 
# Input: 0 → Program stops
while True:
    n=int(input("Enter the number:"))
    if n==0:
        print("Exiting program..")
        break
    print("You entered:",n)