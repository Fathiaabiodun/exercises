# Exercise 1

print ("welcome to my computer quiz!")
playing= input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()
print ("okay! Let's play:)")
score=0

question= input("what does cpu stand for? ")
if question == "central processing unit" : 
    print ('correct')
    score+=1
else:
    print("incorrect")       
 
question= input("what does RAM stand for? ")
if question == "random access memory" : 
    print ('correct')
    score+=1
else:    
    print("incorrect")

print("you got " + str(score) +  " question(s) correctly") 
print("you got " + str((score/2) * 100) +  "  %") 
      

# Exercise 2

import random 

top_of_range= input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 next time")
        quit()

else:
    print("please type a number next time")
    quit()

random_number=random.randint(0,top_of_range) 
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time") 
        continue

    if user_guess==random_number:
        print("You got it!")
        break
    if user_guess> random_number:
        print("You are above the number!")
    else:
        print("you are below the number!")  
print("you got it in", guesses, "guesses")            



# Exercise 3

import random

user_wins=0
computer_wins=0

options=["rock", "paper", "scissors"]

while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input =="q":
        break
    if user_input not in options:
        continue
    random_number= random.randint(0,2)
    computer_pick=options[random_number]
    print("computer picked", computer_pick, ".")

    if user_input=="rock" and computer_pick=="scissors":
        print("You won!")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("You won!")
        user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
        print("You won!")
        user_wins+=1
    else:
        print("you lose!")
        computer_wins +=1    
print("You won", user_wins, "times.") 
print("The computer won", computer_wins, "times.")
print("Goodbye!")           



# Exercise 4

master_pwd=input("What is the master password? ")

def view():
    with open("password.txt", "a") as f:
        f.write(name + "/" + pwd + "/n")

def add():
    name=input("Account name: ")
    pwd=input("Password: ") 

    with open("password.txt", "a") as f:
        f.write(name + "/" + pwd + "/n")

while True:
    mode=input("Would you like to add a new password or view an existing one(view or add) press q to quit? ")


    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="add":  
        add()
    else:
        print("invalid mode.") 
        continue

    
