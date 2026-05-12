import random
options = ["rock", "paper", "scissors"]
computer  = random.choice(options)
player  = input("rock, paper, or scissors?").lower()
print("computer chose:", computer )
if player == computer:
    print("Tie!")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print("You win!")
else:   
    print("You lose!")