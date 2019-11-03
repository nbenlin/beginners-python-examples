import random
import os
from time import sleep

clear = lambda: os.system('cls')
clear()
print("""
*****************************
*****  Gues The Number  *****  
        from 1 to 10 
******************************
""")

random_number = random.randint(1, 10)
turn = 5
turned = 1
while True:
    guess = int(input("Pick a number between 1 and 10\n------>Your guess:"))

    
    if guess < random_number:
        print("\nChecking number")
        for i in range(1, 8):
            print("*", end=" ")
            sleep(0.3)
        clear()

        print("\nYour guess, {} is too low.".format(guess))
        turned += 1
        turn -= 1
    
    elif guess > random_number:
        print("\nChecking number")
        for i in range(1, 8):
            print("*", end=" ")
            sleep(0.3)
        clear()     

        print("\nYour guess, {} is too high.".format(guess))
        turned += 1
        turn -= 1

    else:
        print("\nChecking number")
        sleep(1)
        for i in range(1, 8):
            print("*", end=" ")
            sleep(0.3)
        clear()

        print("\nCongratulations, It took you {} turns to guess my number, which was {}".format(turned, random_number))
        
        choice = input("Do you want play again? < Y/n >")
        if choice == 'n':
            print("Bye bye .. .. .. ..")
            break

    if turn == 0:
        print("Oops!! No turns left. My number was", random_number)       
        
        choice2 = input("Do you want play again? < Y/n >")
        if choice2 == 'n':
            print("Bye bye .. .. .. ..")
            break

