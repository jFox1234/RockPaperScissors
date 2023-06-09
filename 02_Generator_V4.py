import random

items = ["rock", "paper", "scissors"]


# functions go here:
def generator(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "":
            response = random.choice(items)
            return response
        elif response == "xxx":
            print("Thanks for playing!")
            break
        else:
            print("Please press <Enter> to continue, or 'xxx' to end the game.")


generate = generator("Press <Enter> to generate: ")
print(generate)
