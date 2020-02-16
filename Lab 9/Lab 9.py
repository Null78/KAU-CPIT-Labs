# Problem 1
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



# Problem 2
def m(i):
    # Calculate
    sum = 0
    for j in range(1, i + 1):
        sum += j / (j + 1)
    # Return the result
    return sum


def main():
    # Header
    print(format("i", "<20s"),
          format("m(i)", "<10s"))

    # Print output
    for i in range(1, 21):
        print(format(i, "<20d"),
              format(m(i), "<20.4f"))


# Call the main function
main()



# Problem 3
import math


def isValid(side1, side2, side3):
    # Check if the sum of any two sides is greater than the third side.
    condition1 = side1 + side2 > side3
    condition2 = side2 + side3 > side1
    condition3 = side1 + side3 > side2

    # Return True of False
    return condition1 and condition2 and condition3


def area(side1, side2, side3):
    # Calculate p
    p = (side1 + side2 + side3) / 2

    # Calculate area
    area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
    return area


def main():
    # Get three sides
    s1, s2, s3 = eval(input("Enter three sides in double: "))

    # Call isValid
    if isValid(s1, s2, s3):
        print("The area of the triangle is", area(s1, s2, s3))
    else:
        print("Input is invalid")


# Call main function
main()



# Problem 4
def displayPattern(n):
    for i in range(1, n + 1):

        for j in range(n - i):
            print("  ", end=" ")

        for k in range(i, 0, -1):
            print(format(k, "2d"), end=" ")
        print()


def main():
    # Get input
    n = eval(input("Enter line number: "))

    # Call displayPattern function and pass n
    displayPattern(n)


# Call the main function
main()



# Problem 5
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



# Problem 6
def celsiusToFahrenheit(celsius):
    # Calculate and return the result
    return (9/5) * celsius + 32


def fahrenheitToCelsius(fahrenheit):
    # Calculate and return the result
    return (5 / 9) * (fahrenheit - 32)


def main():
    celsius = 40
    fahrenheit = 120

    # Table header
    print(format("Celsius", "<12s"),
          format("Fahrenheit", "<12s"),
          " | ",
          format("Fahrenheit", ">12s"),
          format("Celsius", ">12s"))
    print("----------------------------------------------------------------")

    while celsius >= 31:
        # Call the functions and print the result formated
        print(format(celsius, "<12d"),
              format(celsiusToFahrenheit(celsius), "<12.2f"),
              " | ",
              format(fahrenheit, ">12d"),
              format(fahrenheitToCelsius(fahrenheit), ">12.2f"))
        celsius -= 1
        fahrenheit -= 10


# Call the main function
main()
