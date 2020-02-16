# lab 8

# Problem 1
# Ask the user for the number of students
number = eval(input("Enter the number of students: "))

# Get the first student name and score
# Highest score
name1 = input("Enter a student name: ")
score1 = eval(input("Enter a student score: "))

# Ask the user for student names and scores
# loop one time less than number entered by the user
for i in range(number - 1):
    # Ask the user for the next student name and score
    name = input("Enter a student name: ")
    score = eval(input("Enter a student score: "))

    if score > score1:
        # Check the score of the entered student with the highest score
        name1 = name
        score1 = score

# when the loop stopes
# Display the output
print()  # Empty line
print(f"Top student {name1}'s score is {score1}")



# Problem 2
# Get load amount
loan = eval(input("Enter loan amount, for example 120000.95: "))

# Get number of years
years = eval(input("Enter number of years as an integer, for example 5: "))

# Display the header
print()  # Empty line
# Align to the left with width 20 and type string
print(format("Interest Rate", "<20s"), end="")  # Without new line
print(format("Monthly Payment", "<20s"), end="")  # Without new line
print(format("Total Payment", "<20s"))

# Annual Interest Rate %
air = 5

# loop from 5% to 8%
while air <= 8:
    # Calculate the Monthly interest rate
    mir = air / 1200

    # Calculate mothly payment
    monthlyPayment = loan * mir / (1 - (1 / (1 + mir) ** (years * 12)))

    # Calculate total payment
    totalPayment = monthlyPayment * years * 12

    # Display results
    print(format(air, ">5.3f"), "%",
          format(monthlyPayment, "20.2f"),
          format(totalPayment, "20.2f"))

    # Increase annual interset rate by 1/8
    air += 1/8



# Problem 3
# Ask the user for the number of students
number = eval(input("Enter the number of students: "))

# Get the first student name and score
# Highest score
name1 = input("Enter a student name: ")
score1 = eval(input("Enter a student score: "))

# Get the second student name and score
# Second highest score
name2 = input("Enter a student name: ")
score2 = eval(input("Enter a student score: "))

if score2 > score1:
    # If score2 is higher than score1
    # Swap the variables
    score1, score2 = score2, score1
    name1, name2 = name2, name1


# Ask the user for student names and scores
# loop one time less than number entered by the user
for i in range(number - 2):
    # Ask the user for the next student name and score
    name = input("Enter a student name: ")
    score = eval(input("Enter a student score: "))

    # Check the score of the entered student with the highest score
    if score > score1:
        # the highest student became the second highest
        name2, score2 = name1, score1
        # And the new one is the highest
        name1 = name
        score1 = score

        # Check the new student score with the second highest score
    elif score > score2:
        name2 = name
        score2 = score


# when the loop stopes
# Display the output
print()  # Empty line
print("Top two students: ")
print(f"{name1}'s score is {score1}")
print(f"{name2}'s score is {score2}")



# Problem 4
# Pattern 1
print("\nPattern 1\n")
for i in range(1, 7):
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# Pattern 2
print("\nPattern 2\n")
for i in range(6, 0, -1):
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# Pattern 3
print("\nPattern 3\n")
for i in range(1, 7):

    for j in range(6 - i):
        print(" ", end=" ")

    for k in range(i, 0, -1):
        print(k, end=" ")
    print()

# Pattern 4
print("\nPattern 4\n")
for i in range(6, 0, -1):

    for j in range(6 - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print(k, end=" ")
    print()
