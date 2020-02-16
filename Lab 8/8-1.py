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
