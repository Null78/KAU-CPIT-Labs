import random

# Generate random number between 0 and 2
computer = random.randint(0, 2)

# Ask the user to enter number between 0 and 2
user = eval(input("scissor (0), rock (1), paper (2): "))

# Compare
# A scissor can cut a paper, a rock can knock a scissor, and a paper can wrap a rock.
# if the computer is 0 scissor
if computer == 0:
    if user == 0:
        print("The computer is scissor. You are scissor too. It is a draw.")
    elif user == 1:
        print("The computer is scissor. You are rock. You win.")
    elif user == 2:
        print("The computer is scissor. You are paper. You lost.")
    else:
        print("Wrong selection.")

# if the computer is 1 rock
if computer == 1:
    if user == 0:
        print("The computer is rock. You are scissor. You lost.")
    elif user == 1:
        print("The computer is rock. You are rock too. It is a draw.")
    elif user == 2:
        print("The computer is rock. You are paper. You win.")
    else:
        print("Wrong selection.")

# if the computer is 2 paper
if computer == 2:
    if user == 0:
        print("The computer is paper. You are scissor. You win.")
    elif user == 1:
        print("The computer is paper. You are rock. You lost.")
    elif user == 2:
        print("The computer is paper. You are paper too. It is a draw.")
    else:
        print("Wrong selection.")
