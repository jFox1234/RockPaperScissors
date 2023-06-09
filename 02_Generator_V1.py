import random
play = ""

while not play == "xxx":
    play = input("Press <Enter> to generate: ")
    generate = random.randint(1, 3)
    if generate == 1:
        item = "paper"
        print(item)
    elif generate == 2:
        item = "scissors"
        print(item)
    else:
        item = "rock"
        print(item)
