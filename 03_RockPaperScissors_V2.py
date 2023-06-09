# computer input for testing purposes
computer = input("Enter computer input: ").lower()


# functions go here:
def win_lose(question):
    valid = False
    while not valid:
        response = input(question).lower()
        # calculate winner and loser
        if response == "rock" and computer == "rock" or response == "r" and computer == "rock":
            response = "drawn"
        elif response == "rock" and computer == "scissors" or response == "r" and computer == "scissors":
            response = "won"
        elif response == "rock" and computer == "paper" or response == "r" and computer == "paper":
            response = "lost"
        if response == "paper" and computer == "paper" or response == "p" and computer == "paper":
            response = "drawn"
        elif response == "paper" and computer == "rock" or response == "p" and computer == "rock":
            response = "won"
        elif response == "paper" and computer == "scissors" or response == "p" and computer == "scissors":
            response = "lost"
        if response == "scissors" and computer == "scissors" or response == "s" and computer == "scissors":
            response = "drawn"
        elif response == "scissors" and computer == "paper" or response == "s" and computer == "paper":
            response = "won"
        elif response == "scissors" and computer == "rock" or response == "s" and computer == "rock":
            response = "lost"
        return response


# asks for rock paper or scissors
rps = win_lose("Enter paper, scissors, or rock? R/P/S ")
print("The computer chose: {}".format(computer))
print("You have {} against the computer".format(rps))
