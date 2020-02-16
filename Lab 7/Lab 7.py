# lab 7

# Problem 1
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



# Problem 2
# Table header
print("--------------------------------------------------------")
# print kilograms to the left with width 10 and type string
print(format("kilograms", "<10s"),
    # print pounds to the right with width 10 and type string
    format("pounds", ">10s"),
    # spcae between columns
    "     |     ",
    # print pounds to the left with width 10 and type string
    format("pounds", "<10s"),
    # print kilograms to the right with width 10 and type string
    format("kilograms", ">10s"))
print("--------------------------------------------------------")

# Defain counting variables
kg = 1
pnd = 20

while kg <= 199:
    # Calculate
    kg_to_pnd = kg * 2.2
    pnd_to_kg = pnd * 0.45

    # Display the result
    # print kg to the left with width 10 and type integer
    print(format(kg, "<10d"),
    # print kg_to_pnd to the right with width 10 rounded by 1 and type float
    format(kg_to_pnd, ">10.1f"),
    # spcae between columns
    "     |     ",
    # print pnd to the left with width 10 and type integer
    format(pnd, "<10d"),
    # print pnd_to_kg to the right with width 10 rounded by 2 and type float
    format(pnd_to_kg, ">10.2f"))

    # Add 2 to kg and 5 to pnd
    kg += 2
    pnd += 5



# Problem 3
# Table header
print("--------------------------------------------------------")
# print Miles to the left with width 10 and type string
print(format("Miles", "<10s"),
    # print Kilometers to the right with width 10 and type string
    format("Kilometers", ">10s"),
    # spcae between columns
    "     |     ",
    # print Kilometers to the left with width 10 and type string
    format("Kilometers", "<10s"),
    # print Miles to the right with width 10 and type string
    format("Miles", ">10s"))
print("--------------------------------------------------------")

# Defain counting variables
miles = 1
km = 20

while miles <= 10:
    # Calculate
    miles_to_km = miles * 1.609
    km_to_miles = km / 1.609

    # Display the result
    # print miles to the left with width 10 and type integer
    print(format(miles, "<10d"),
    # print miles_to_km to the right with width 10 rounded by 3 and type float
    format(miles_to_km, ">10.3f"),
    # spcae between columns
    "     |     ",
    # print km to the left with width 10 and type integer
    format(km, "<10d"),
    # print km_to_miles to the right with width 10 rounded by 3 and type float
    format(km_to_miles, ">10.3f"))

    # Add 1 to miles and 5 to km
    miles += 1
    km += 5



# Problem 4
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
