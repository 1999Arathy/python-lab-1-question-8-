#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right

import random
x = random.randrange(1,10)
print(x)
guess = int(input("enter any single digit number"))
if(x==guess):
    print("You gussed exactly correct")
elif(x>guess):
    print("You gussed too low")
else:
     print("You gussed too high")