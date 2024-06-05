import random
#initial scores must be zero
user_scores=0
computer_scores=0
options=["rock","paper","scissor"]
number_of_guesses=0
tie=0
while number_of_guesses<5:
    
    user_input=input("Type Rock, Paper or Scissor or Type Q to quit the game ").lower()
    if user_input==" q":
        break
    if user_input not in options :
        print("Type Rock/Paper/Scissor Only")
        continue
    number_of_guesses+=1
    #Rock:0, Paper:1, Scissor:2
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("computer Picks", computer_pick + "." )
    if user_input==computer_pick:
        print("Its a Tie")
        tie+=1
        continue
    elif user_input=="scissor" and computer_pick=="paper":
        print("You won")
        user_scores+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("You won")
        user_scores+=1
    elif user_input=="rock" and computer_pick=="scissor":
        print("You won")
        user_scores+=1
    else:
        print("You lost")
        computer_scores+=1
print("You scored", str(user_scores)+ "/5.")
print("Computer scores", computer_scores,"/5")
print("Total Ties: ", tie)
if user_scores>=3:
    print("winner".upper())
else:
    print("Better luck next time")



    
    
