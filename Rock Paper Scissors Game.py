import random
opt = ["Rock" , "Paper" , "Scissors"]

play = 'y'

while(play=='y'):
    your_choice = input("Choose Rock , Paper or Scissors:")
    Computer_choice = random.choice(opt)

    print("You choose", your_choice)
    print("computer choose", Computer_choice)

    if your_choice == Computer_choice:
        print("It's a tie!") 
    
    elif your_choice == "Rock" and Computer_choice == "Scissors":
        print("You Win!")
    
    elif your_choice == "Paper" and Computer_choice == "Rock":
        print("You Win!")
    
    elif your_choice == "Scissors" and Computer_choice == "Paper":
        print("You Win!")
    
    else:
        print("Computer Wins!")
    print()
    print('Do you want to play more? Pres y/n')
    play=input()
    if play != "y":
        print("Thank you!!")

    
    

    