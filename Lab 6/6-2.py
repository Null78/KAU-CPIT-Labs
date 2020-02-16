import random
# Generate two random numbers under 100
number1 = random.randint(0,99)
number2 = random.randint(0,99)

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
