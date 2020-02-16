# Ask the user to enter a number
number = eval(input("Enter a number (0: for end of input): "))

# Defain count variable
count = 1

# Defain the largest number with value of the entered number
max = number

# Define a while loop and set its condition to number != 0
# (while number is not equal to 0)
while number != 0:
    # Ask the user for the next number
    number = eval(input("Enter a number (0: for end of input): "))

    if number > max:
        # If the new number is larger change the max to it
        max = number
        # Reset the count
        count = 1

    elif number == max:
        # If the max number occurrences againg
        # Increase count by 1
        count += 1


# When the loop stops (number = 0)
# Display the result
print("The largest number is", max)
print("The occurrence count of the largest number is", count)
