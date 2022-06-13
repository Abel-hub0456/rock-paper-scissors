import random

print("Hi! Welcome to the game Rock Paper Scissors.")


while True:
    possible_options = ["Rock", "Paper", "Scissors"]

    #requests for user's choice
    user_option = input("R for Rock\nP for paper\nS for Scissors\nMake your choice: ")
    print("")

    #check if user input is valid
    if user_option.lower() not in ["r", "p", "s"]:
        print("You made a wrong choice.")
        continue

    #computer makes a random choice
    computer_option = random.choice(possible_options)
    if user_option.lower() == "r":
        print("You chose Rock")
        user_option = "Rock"
    elif user_option.lower() == "p":
        print("You chose Paper")
        user_option = "Paper"
    elif user_option.lower() == "s":
        print("You chose Scissors")
        user_option = "Scissors"
    print("Player (" + user_option + ") : " + "CPU (" + computer_option + ")")

    #check for winner
    if user_option == computer_option:
        print("It's a tie!")
        print("")
        continue
    elif user_option == "Rock":
        if computer_option == "Scissors":
            print("Rock smashes Scissors! You win!")
            break
        else:
            print("Paper covers Rock! You lose.")
            break
    elif user_option == "Paper":
        if computer_option == "Rock":
            print("Paper covers Rock! You win!")
            break
        else:
            print("Scissors cuts Paper! You lose.")
            break
    elif user_option == "Scissors":
        if computer_option == "Paper":
            print("Scissors cuts Paper! You win!")
            break
        else:
            print("Rock smashes Scissors! You lose.")
            break
