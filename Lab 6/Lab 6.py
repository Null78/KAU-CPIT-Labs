# lab 6

# Problem 1
import math

# Get inputs
a, b, c = eval(input("Enter a, b, c: "))

# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# Check if it's positive -> two roots
if discriminant > 0:
    # Calculate the roots
    root1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    root2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    # Display the result
    print("The roots are", root1, "and", root2)

# if it is 0 -> one root
elif discriminant == 0:
    # Calculate the root
    root1 = (-b) / (2 * a)
    # Display the result
    print("The roots is", root1)

# otherwise, no roots
else:
    print("The equation has no real roots")



# Problem 2
import random

# Generate two random numbers under 100
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# Ask the user to answer
answer = eval(input(f"What is {number1} + {number2}? "))

# Check the user answer, if it's true, print true
correct_answer = number1 + number2
if answer == correct_answer:
    print(f"{number1} + {number2} = {answer} is True")

# else, print false and display the correct_answer
else:
    print(f"{number1} + {number2} = {answer} is False")
    print("The correct answer is", correct_answer)



# Problem 3
# Get package 1 info
p1_size, p1_price = eval(input("Enter weight and price for package 1: "))

# Get package 2 info
p2_size, p2_price = eval(input("Enter weight and price for package 2: "))

# Calculate 1 kg price for package 1
p1 = p1_price / p1_size

# Calculate 1 kg price for package 1
p2 = p2_price / p2_size

# Check the better price and display the output
if p1 < p2:
    print("Package 1 has the better price.")
elif p1 > p2:
    print("Package 2 has the better price.")
else:
    print("Package 1 and Package 2 are the same.")



# Problem 4
import random

# Generate random number between 0 and 2
computer = random.randint(0, 2)

# Ask the user to enter number between 0 and 2
user = eval(input("scissor (0), rock (1), paper (2): "))

# Compare
# A scissor can cut a paper, a rock can knock a scissor, and a paper can wrap a rock.
if computer == 0:
    # if the computer is 0 scissor
    if user == 0:
        print("The computer is scissor. You are scissor too. It is a draw.")
    elif user == 1:
        print("The computer is scissor. You are rock. You win.")
    elif user == 2:
        print("The computer is scissor. You are paper. You lost.")
    else:
        print("Wrong selection.")

if computer == 1:
    # if the computer is 1 rock
    if user == 0:
        print("The computer is rock. You are scissor. You lost.")
    elif user == 1:
        print("The computer is rock. You are rock too. It is a draw.")
    elif user == 2:
        print("The computer is rock. You are paper. You win.")
    else:
        print("Wrong selection.")

if computer == 2:
    # if the computer is 2 paper
    if user == 0:
        print("The computer is paper. You are scissor. You win.")
    elif user == 1:
        print("The computer is paper. You are rock. You lost.")
    elif user == 2:
        print("The computer is paper. You are paper too. It is a draw.")
    else:
        print("Wrong selection.")
