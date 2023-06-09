# computer input for testing purposes
computer = input("Enter computer input: ").lower()

# asks for rock paper or scissors
rps = input("Enter paper, scissors, or rock? rock/paper/scissors ").lower()

# calculates win, loss, or draw
if rps == "rock" and computer == "rock":
    output = "draw"
    print(output)
elif rps == "rock" and computer == "scissors":
    output = "win"
    print(output)
elif rps == "rock" and computer == "paper":
    output = "lose"
    print(output)
if rps == "paper" and computer == "paper":
    output = "draw"
    print(output)
elif rps == "paper" and computer == "rock":
    output = "win"
    print(output)
elif rps == "paper" and computer == "scissors":
    output = "lose"
    print(output)
if rps == "scissors" and computer == "scissors":
    output = "draw"
    print(output)
elif rps == "scissors" and computer == "paper":
    output = "win"
    print(output)
elif rps == "scissors" and computer == "rock":
    output = "lose"
    print(output)
