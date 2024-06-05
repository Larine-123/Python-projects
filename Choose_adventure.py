name=input("Type your name: ")
print("Welcome".upper(),name.upper(),"to this adventure!!".upper())
answer=input("You are at the end of the road. Which path would you take left or righ? ")
if answer.lower()=="left":
    answer=input("You went left . Now you are in danger. Will you turn back or take risk?( Back/risk) ")
    if answer.lower()=='back':
        print("You lost")
    elif answer.lower()=='risk':
        print("You won")
    else:
        print("Type a valid option.")

elif answer.lower()=="right":
    answer=input("You went right . Now you met a stranger. Will you talk or not talk?( yes/no) ")
    if answer.lower()=='yes':
        print("You won")
    elif answer.lower()=='no':
         print("You lost")
    else:
        print("Type a valid option.")
    
else:
    print("Type a valid option.")
print("Bye",name)