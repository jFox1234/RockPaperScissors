# functions go here:
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "y" or response == "yes":
            response = "yes"
            return response
        elif response == "n" or response == "no":
            response = "no"
            return response

        else:
            print("Please answer Y/N ")


# ask user if they need instructions:
show_instructions = yes_no("Do you need instructions? Y/N ")

# returns the users response:
print("You chose '{}'".format(show_instructions))

# print answer from function:
if show_instructions == "yes":
    print("*** Instructions ***")
    print()
    print("Continue")
