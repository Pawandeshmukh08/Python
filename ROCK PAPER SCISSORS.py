import random

print("Rock...")
print("paper...")
print("scisssors...")

player=input("Player, make your move:").lower()

rand_num = random.randint(0,2)
if rand_num==0:
    computer="rock"
elif rand_num==1:
    computer="paper"
else:
    computer="scissors"
print(f"Computer plays {computer}")

if player==computer:
    print("It's a Tie")
elif player=="rock":
    if computer=="scissors":
        print("Player Wins")
    elif computer=="paper":
        print("Computer Wins")
elif player=="paper":
    if computer=="scissors":
        print("Computer Wins")
    elif computer=="rock":
        print("player Wins")
elif player=="Scissors":
    if computer=="rock":
        print("Computer Wins")
    elif computer=="paper":
        print("Player Wins")
else:
    print("Something went wrong")
