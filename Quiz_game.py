print("Welcome to the quiz".upper())

#asking the user  whether he wants to play or notyes

playing=input("Do you want attend this Quiz? ")
#If the person does ot wants to play 
if playing.lower()!='yes':
    quit()
print("Lets start:")

#add scores
score=0
#questions and answer
answer=input("What is the Holy Book of Christians? ")
if answer.lower()=='the bible':
    print("Correct answer.")
    score=score+1
else:
    print("Incorrect.")

answer=input("What is the national bird of India ")
if answer.lower()=='peacock':
    print("Correct answer.")
    score=score+1
else:
    print("Incorrect.")

answer=input("What is the largest river in the world? ")
if answer.lower()=='nile':
    print("Correct answer.")
    score=score+1
else:
    print("Incorrect.")

answer=input("What is the national animal of India? ")
if answer.lower()=='tiger':
    print("Correct answer.")
    score=score+1
else:
    print("Incorrect.")

print("You scored " + str(score)+ "/4")
percentage=(score/4)*100
print("You scored " + str(percentage)+"%")

