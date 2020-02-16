import random


def printMatrix(n):
    # For each row
    for row in range(n):
        # For each column
        for colum in range(n):
            # Get random number 0 or 1
            value = random.randint(0, 1)
            # Print the value
            print(value, end=" ")
        print()  # New line


def main():
    # Get input
    n = eval(input("Enter n: "))

    # Call printMatrix function and pass n
    printMatrix(n)


# Call the main function
main()
