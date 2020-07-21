import random

random_num=random.randint(1,10)

guess=None

while True:
    guess=int(input("Guess the number again:"))
    if guess<random_num:
        print("Too Low")
    elif guess>random_num:
        print("Too High")
    else:
        print("You Won")
        play_again=input("Do you wanna play agaian? (y/n)")
        if play_again=="y":
            random_num=random.randint(1,10)
            guess=None
            
        else:
            print("Thankyou for playing")
            break
        

