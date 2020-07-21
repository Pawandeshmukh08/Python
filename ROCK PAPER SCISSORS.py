import random

player_wins=0
computer_wins=0
winning_score=3


while player_wins<winning_score and computer_wins<winning_score:
    print(f"player Score: {player_wins} and Computer Score: {computer_wins}")
    print("Rock...")
    print("paper...")
    print("scisssors...")

    player=input("Player, make your move:").lower()

    if player=="quit" or player=="exit" or player=="q":
        break

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
             player_wins+=1
         elif computer=="paper":
            print("Computer Wins")
            computer_wins+=1

    elif player=="paper":
        if computer=="scissors":
            print("Computer Wins")
            computer_wins+=1
        elif computer=="rock":
            print("player Wins")
            player_wins+=1

    elif player=="Scissors":
        if computer=="rock":
            print("Computer Wins")
            computer_wins+=1
        elif computer=="paper":
            print("Player Wins")
            player_wins+=1
    else:
        print("Something went wrong")


if player_wins==winning_score:
    print("Congrats you won")
elif player_wins==computer_wins:
    print("IT'S A TIE")
else:
    print("OH NO !!")

print(f"Player Score: {player_wins} and Computer Score: {computer_wins}")
