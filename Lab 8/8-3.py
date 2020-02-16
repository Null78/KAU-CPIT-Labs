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
