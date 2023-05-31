# ask user if they need instructions:
show_instructions = input("Do you need instructions? Y/N ").lower()

# print answer based on variable input:
if show_instructions == "y" or show_instructions == "yes":
    print("*** Instructions ***")
    print()
    print("Continue")
elif show_instructions == "n" or show_instructions == "no":
    print("Continue")
else:
    print("Please answer Y/N ")
