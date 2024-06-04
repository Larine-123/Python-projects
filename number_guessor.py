import random

#to enter the range 
top_no_range=input("Enter a number for the top most range:")
#check number entered i a idigit
if top_no_range.isdigit():
    top_no_range=int(top_no_range)
    if top_no_range<=0:
        print("Enter a number greater than 0.")
        quit()
else:
    print("Enter number only.")
    quit()
random_number=random.randint(1,top_no_range)
guess=0
while True:
    #to find number of guesses
    guess+=1
    user_guess=input("Guess number.. ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Enter a number only.")
        continue
    #compare user input and randomly generated number
    if user_guess==random_number:
        print("Your guess is accurate..")
        print("Total number of guesses: ",guess)
        quit()
    elif user_guess>random_number:
        print("Your number is larger ")
    else :
        print("Your number is smaller")


