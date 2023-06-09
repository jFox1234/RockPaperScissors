import random
play = ""


while not play == "xxx":
    play = input("Press <Enter> to generate: ").lower()
    if play == "":
        generate = random.randint(1, 3)
        if generate == 1:
            item = "paper"
        elif generate == 2:
            item = "scissors"
        else:
            item = "rock"
        print("The computer chose {}".format(item))
    elif play == "xxx":
        print("Thanks for playing!")
        break
    else:
        print("Please press <Enter> to continue, or 'xxx' to end the game.")
        continue
