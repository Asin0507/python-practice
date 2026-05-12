import random
secret =random . randint(1,10)
while True :
    guess = int(input("guess a number between 1 and 10:"))
    if guess > secret:
        print("too high!")
    elif guess < secret:
        print("too low!")
    else:
        print("correct")
        break