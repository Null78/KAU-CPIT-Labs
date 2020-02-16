# Defain displaySortedNumbers function
def displaySortedNumbers(num1, num2, num3):
    # num1 is larger than num2 swap them
    if num1 > num2:
        num1, num2 = num2, num1

    # num2 is larger than num3 swap them
    if num2 > num3:
        num2, num3 = num3, num2

    # num1 is larger than num2 swap them
    if num1 > num2:
        num1, num2 = num2, num1

    # Display the output
    print("The sorted numbers are", num1, num2, num3)


# Defain main function
def main():
    # Get three numbers
    num1, num2, num3 = eval(input("Enter three integers: "))
    # Call displaySortedNumbers function and pass the three numbers
    displaySortedNumbers(num1, num2, num3)


# Call main function
main()
