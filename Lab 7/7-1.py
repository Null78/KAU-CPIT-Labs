# Ask the user to enter a number
number = eval(input("Enter an integer, the input ends if it is 0: "))

# Defain two variables to count postive and negative numbers
count_positives = 0
count_negatives = 0
# Define a variable to store the sum of all entered numbers
total = 0

# Define a while loop and set its condition to number != 0
# (while number is not equal to 0)
while number != 0:

    if number > 0:
        # If the number is positive
        count_positives += 1
    elif num < 0:
        # If the number is negative
        count_negatives += 1

    # Add number to total
    total += number
    # Ask the user to enter the next number
    number = eval(input("Enter an integer, the input ends if it is 0: "))

# When the loop ends (number = 0)
if (count_negatives + count_positives) == 0:
    # If there is no other inputs
    print("No numbers are entered except 0")

else:
    # otherwise, there is inputs
    # Calculate the average
    average = total / (count_positives + count_negatives)
    # Display the result
    print("The number of positives is", count_positives)
    print("The number of negatives is", count_negatives)
    print("The total is", total)
    print("The average is", average)
