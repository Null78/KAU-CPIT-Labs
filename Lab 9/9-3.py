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
