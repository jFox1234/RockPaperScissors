import random


# functions go here:
def generator(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "":
            response = random.randint(1, 3)
            return response
        elif response == "xxx":
            print("Thanks for playing!")
            break
        else:
            print("Please press <Enter> to continue, or 'xxx' to end the game.")


play = generator("Press <Enter> to generate: ")

if generator == 1:
    item = "paper"
elif generator == 2:
    item = "scissors"
else:
    item = "rock"
print(item)
