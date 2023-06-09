import random
items = ["rock", "paper", "scissors"]


# functions go here:
def win_lose(question):
    valid = False
    while not valid:
        response = input(question).lower()
        # calculate winner and loser
        if response == "rock" and computer == "rock" or response == "r" and computer == "rock":
            response = "drawn"
            return response
        elif response == "rock" and computer == "scissors" or response == "r" and computer == "scissors":
            response = "won"
            return response
        elif response == "rock" and computer == "paper" or response == "r" and computer == "paper":
            response = "lost"
            return response
        if response == "paper" and computer == "paper" or response == "p" and computer == "paper":
            response = "drawn"
            return response
        elif response == "paper" and computer == "rock" or response == "p" and computer == "rock":
            response = "won"
            return response
        elif response == "paper" and computer == "scissors" or response == "p" and computer == "scissors":
            response = "lost"
            return response
        if response == "scissors" and computer == "scissors" or response == "s" and computer == "scissors":
            response = "drawn"
            return response
        elif response == "scissors" and computer == "paper" or response == "s" and computer == "paper":
            response = "won"
            return response
        elif response == "scissors" and computer == "rock" or response == "s" and computer == "rock":
            response = "lost"
            return response
        else:
            print("Incorrect Input! ")


def generator(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "":
            response = random.choice(items)
            return response
        elif response == "xxx":
            response = "xxx"
            return response
        else:
            print("Please press <Enter> to continue, or 'xxx' to end the game.")


# asks for rock paper or scissors
computer = generator("Press <Enter> to play or 'xxx' to quit: ")
# computer input

if computer == "rock" or computer == "scissors" or computer == "paper":
    rps = win_lose("Enter paper, scissors, or rock? R/P/S ")
    print("The computer chose: {}".format(computer))
    print("You have {} against the computer".format(rps))
elif computer == "xxx":
    print("Thanks for playing!")
else:
    rps = ""
